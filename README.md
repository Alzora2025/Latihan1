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






FITUR UTAMA 
1.Unggah File:
• Format yang didukung: CSV, XLSX, XLS, PDF.
File akan disimpan di folder uploads.

2.Analisis Otomatis:
•Rasio keuangan seperti ROE , NPM , DER , PER , dan PBV dihitung secara otomatis.
Penilaian dan rekomendasi (Beli, Tahan, Hindari) diberikan berdasarkan skor.

3.Hasil:
• Hasil analisis ditampilkan dalam tabel HTML.





Catatan Penting:

1.Kolom Wajib: Pastikan file memiliki kolom:

Net_Income, Revenue, Equity, Total_Debt, Stock_Price, EPS, Book_Value_Per_Share.

2.Kesalahan Umum:

Jika file tidak memiliki kolom yang sesuai, aplikasi akan memberikan pesan error.
Untuk PDF, pastikan tabel dalam format yang dapat dikenal oleh Tabula.

3. Pengembangan Lebih Lanjut:

Tambahkan fitur ekspor hasil analisis ke PDF atau Excel.
Tingkatkan validasi data untuk memastikan hasil analisis lebih akurat.



***Jika Anda membutuhkan bantuan tambahan untuk menjalankan atau mengembangkan aplikasi ini, beri tahu saya! 😊 "**
