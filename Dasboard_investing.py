from flask import Flask, render_template, request
import pandas as pd
import os
from werkzeug.utils import secure_filename
import tabula

app = Flask(__name__)

# Ensure an upload folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to calculate key financial ratios
def calculate_ratios(data):
    data['ROE (%)'] = (data['Net_Income'] / data['Equity']) * 100
    #Corrected indentation for the following lines
    data['NPM (%)'] = (data['Net_Income'] / data['Revenue']) * 100
    data['DER'] = data['Total_Debt'] / data['Equity']
    data['PER'] = data['Stock_Price'] / data['EPS']
    data['PBV'] = data['Stock_Price'] / data['Book_Value_Per_Share']
    data['Score'] = ((data['ROE (%)'] >= 15).astype(int) +
                     (data['NPM (%)'] >= 10).astype(int) +
                     (data['DER'] <= 1).astype(int) +
                     (data['PER'] <= 20).astype(int) +
                     (data['PBV'] <= 1.5).astype(int)) * 20
    data['Recommendation'] = data['Score'].apply(lambda x: 'Buy' if x >= 80 else 'Hold' if x >= 60 else 'Avoid')
    return data

def read_file(filepath, file_ext):
    if file_ext == 'csv':
        return pd.read_csv(filepath)
    elif file_ext in {'xlsx', 'xls'}:
        return pd.read_excel(filepath)
    elif file_ext == 'pdf':
        # Extract tables from PDF and combine into a single DataFrame
        tables = tabula.read_pdf(filepath, pages='all', multiple_tables=True, pandas_options={'dtype': str})
        return pd.concat(tables, ignore_index=True)
    else:
        raise ValueError("Unsupported file format")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded"

        file = request.files['file']
        if file.filename == '':
            return "No file selected"

        if not allowed_file(file.filename):
            return "Unsupported file format"

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Get file extension
            file_ext = filename.rsplit('.', 1)[1].lower()

            # Load data
            data = read_file(filepath, file_ext)

            # Ensure required columns exist
            required_columns = ['Net_Income', 'Revenue', 'Equity', 'Total_Debt', 'Stock_Price', 'EPS', 'Book_Value_Per_Share']
            if not all(col in data.columns for col in required_columns):
                return "Uploaded file must contain the following columns: " + ", ".join(required_columns)

            # Convert numerical columns to the correct data type
            data[required_columns] = data[required_columns].apply(pd.to_numeric, errors='coerce')

            # Calculate financial ratios
            analyzed_data = calculate_ratios(data)

            # Render the results table
            return render_template('dashboard.html', tables=[analyzed_data.to_html(classes='data', header="true")], titles=analyzed_data.columns.values)

        except Exception as e:
            return f"Error processing file: {str(e)}"

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
