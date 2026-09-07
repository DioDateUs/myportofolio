Nama : Deodatus Kevin Sihaloho

NPM : 2506590920

Kelas : PBP F

## Setup

Sebelum memulai, pastikan Python 3.13 (atau versi lain yang kompatibel dengan `requirements.txt`) sudah terpasang.

### 1. Buat virtual environment

Buka terminal di folder proyek, lalu jalankan:

```bash
python -m venv env
```

### 2. Aktifkan virtual environment

- PowerShell: `env\Scripts\Activate.ps1`
- Command Prompt: `env\Scripts\activate.bat`
- Terminal bawaan VSCode: `env/Scripts/Activate`

### 3. Pasang seluruh dependency

```bash
pip install -r requirements.txt
```

### 4. Periksa konfigurasi & migrasikan database

Sebelum server dijalankan, pastikan tidak ada error dengan menjalankan:

```bash
python manage.py check
python manage.py migrate
```

### 5. Jalankan server

```bash
python manage.py runserver
```

Setelah itu, buka browser dan akses `http://127.0.0.1:8000`.

### Tugas 1

1. Ya, karena daripada menggunakan elemen &lt;div> di semua tempat, elemen semantik bisa memisahkan fungsi blok kode nya seperti &lt;section id="pengalaman"> yang langsung menjelaskan bahwa itu adalah untuk section pengalaman sehingga dapat lebih mudah di akses jika ada yang ingin diubah di bagian pengalaman

2. Mungkin karena terbiasa di tailwind, yang kalo mau bikin elemen responsif bisa tinggal tempel utility class kayak flex flex-col md:flex-row, jadinya ketika memakai CSS biasa lagi harus membiasakan diri lagi jadi ketika mengerjakan bolak balik HTML dan css, terus buat nentuin ukuran juga harus atur margin dan padding nya, untuk evaluasinya, mungkin karena udah kebiasa menggunakan tailwind, jadinya udah ada insting buat liat kalo di dekstop normal, di layar kecil aman ga ya, kalo emang terlalu sempit, elemen yg awalnya horizontal bisa diubah ke vertikal, buat prioritasin mana yang paling atas itu ngebayangin sebagai user apa yang pengen diliat pertama kali, contohnya di bagian pengalaman, pasti yang pengen diliat organisasinya dulu kan, jadi nama nya ditaruh di paling atas.

3. Karena semua data nya msaish hardcoded, jadinya kebayang kalo udah ditambahin section lain, pasti panjang banget, kalo ada yang mau dibenerin juga masih harus masukin di source code nya langsung (makanya belom nambahin section lain hehe), karena ga ada JavaScript juga, belom bisa bikin filter atau semacamnya,  Mungkin fungsi yang pengen ditambahin sesimpel dashboard kali ya, atau mungkin bikin CMS simple biar bisa nambahin atau edit data nya dari browser biar ga perlu nyentuh kode html nya lagi

Dalam pengerjaan nya, saya tidak menggunakan AI sama sekali, seperti pada penambahan section pengalaman, saya menggunakan referensi berdasarkan web yang pernah saya buat ketika awal belajar saya membuat web, ketika ada kesalahan, saya mengecek kembali apakah ada perbedaan yang saya lakukan sekarang dan apa yang ada pada kode saya dahulu. Saya juga masih melihat web seperti W3schools, geeksforgeeks, serta web lainnya sebagai panduan, seperti untuk melihat panduan penggunaan open pada html