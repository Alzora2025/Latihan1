Langkah-langkah menggunakannya

1. Persiapkan Lingkungan venp:
° Pastikan Anda memiliki
° lingkungan virtual python yang terinstal 

* cara pemasangan untuk mac dan Linux 
python -m venv venv
source venv/bin/activate

* pemasangan di windows
venv\\Scripts\\activate  
venv\\Sc

2. Instal perpustakaan yang diperlukan:
pip install flask pandas tabula-py werkzeug openpyxl

• Untuk membaca file PDF, pastikan Java terinstal karena tabula-pymemerlukannya.

3. Buat Folder untuk Unggahan File:

Pastikan folder uploads dibuat secara otomatis dengan kode, atau buat manual jika diperlukan.

4. Simpan File HTML untuk Templat:

Buat folder templatesdi direktori yang sama dengan file Python.
Tambahkan dua file:
•upload.html : Formulir untuk mengunggah file.
•dashboard.html : Template untuk menampilkan hasil analisis.

5.Jalankan Aplikasi:
• python app.py
• Akses di browser: http://127.0.0.1 : 5000 
