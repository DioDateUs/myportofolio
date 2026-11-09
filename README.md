Nama : Deodatus Kevin Sihaloho

NPM : 2506590920

Kelas : PBP F

## Deskripsi Proyek

Website ini adalah portofolio pribadi interaktif yang dirancang untuk menampilkan profil, latar belakang akademik, untuk sekarang, isinya hanya pengalaman organisasi, namun akan bertambah seiring waktu. Proyek ini ditujukan untuk tugas individu mata kuliah Pemrograman Berbasis Platform Semester Gasal 2026/2027.

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

```bas
python manage.py runserver
```

Setelah itu, buka browser dan akses `http://127.0.0.1:8000`.

## Progres Mingguan

1. Week 1: Setup Django dan template awal portofolio
2. Week 2: Penambahan section baru (pengalaman)
3. Week 3: Perubahan menjadi MVT dan penambahan section baru (interests)
4. Week 4: Penggunaan modelform dan JSON
5. Week 5: Penerapan role editor dan register/login, penambahan toggle_star
6. Week 6: Penerapan pencarian menggunakan AJAX

## Tugas

### Tugas 1

1. Ya, karena daripada menggunakan elemen &lt;div> di semua tempat, elemen semantik bisa memisahkan fungsi blok kode nya seperti &lt;section id="pengalaman"> yang langsung menjelaskan bahwa itu adalah untuk section pengalaman sehingga dapat lebih mudah di akses jika ada yang ingin diubah di bagian pengalaman

2. Mungkin karena terbiasa di tailwind, yang kalo mau bikin elemen responsif bisa tinggal tempel utility class kayak flex flex-col md:flex-row, jadinya ketika memakai CSS biasa lagi harus membiasakan diri lagi jadi ketika mengerjakan bolak balik HTML dan css, terus buat nentuin ukuran juga harus atur margin dan padding nya, untuk evaluasinya, mungkin karena udah kebiasa menggunakan tailwind, jadinya udah ada insting buat liat kalo di dekstop normal, di layar kecil aman ga ya, kalo emang terlalu sempit, elemen yg awalnya horizontal bisa diubah ke vertikal, buat prioritasin mana yang paling atas itu ngebayangin sebagai user apa yang pengen diliat pertama kali, contohnya di bagian pengalaman, pasti yang pengen diliat organisasinya dulu kan, jadi nama nya ditaruh di paling atas.

3. Karena semua data nya masih hardcoded, jadinya kebayang kalo udah ditambahin section lain, pasti panjang banget, kalo ada yang mau dibenerin juga masih harus masukin di source code nya langsung (makanya belom nambahin section lain hehe), karena ga ada JavaScript juga, belom bisa bikin filter atau semacamnya,  Mungkin fungsi yang pengen ditambahin sesimpel dashboard kali ya, atau mungkin bikin CMS simple biar bisa nambahin atau edit data nya dari browser biar ga perlu nyentuh kode html nya lagi

Dalam pengerjaan nya, saya tidak menggunakan AI sama sekali, seperti pada penambahan section pengalaman, saya menggunakan referensi berdasarkan web yang pernah saya buat ketika awal belajar saya membuat web, ketika ada kesalahan, saya mengecek kembali apakah ada perbedaan yang saya lakukan sekarang dan apa yang ada pada kode saya dahulu. Saya juga masih melihat web seperti W3schools, geeksforgeeks, serta web lainnya sebagai panduan, seperti untuk melihat panduan penggunaan open pada html

### Tugas 2

1. Alur proses MVT (Model-View-Template) pada Django saat pengguna membuka halaman portofolio baru:
- Browser pengguna mengirimkan HTTP GET Request ke server.
- urls.py Proyek (portofolio/urls.py) membaca domain utama dan mengarahkan rute ke modul aplikasi yang sesuai.
- urls.py Aplikasi (main/urls.py) mencocokkan endpoint (misal: 'project/' atau 'experience/') lalu memanggil fungsi View yang tepat.
- View (views.py) menerima request dan meminta data yang dibutuhkan ke Model (models.py).
- Model berkomunikasi dengan Database  untuk mengambil data lalu mengembalikan objek/query ke View.
- View mengemas data tersebut ke dalam dictionary context dan memanggil file Template yang dituju.
- Django Template Engine merender data dari context ke dalam kerangka HTML (templates/project.html).
- View membungkus hasil akhir render tersebut menjadi HTTP Response utuh (HTML, CSS, dan Gambar).
- Browser pengguna membaca kode HTML tersebut dan merender tampilan visual halaman di layar.

2. Dengan tidak melakukan hard-code pada data, kita bisa mengubah, menambahkan, atau menghapus data melalui panel admin, jadi bahkan tidak perlu membuka file kode sama sekali. Data yang digunakan di satu model, dapat digunakan kembali di model lainnya dengan menyesuaikan isi yang ditampilkan. Jika ada yang ingin diubah pada tampilan, tidak perlu takut ada data yang hilang karena data ada pada tempat yang berbeda, begitu juga sebaliknya jika ingin mengubah data, tidak perlu takut tampilan berubah

3. Makemigration membaca setiap perubahan yang dilakukan pada models.py, setelah terdeteksi, akan tercatat di dalam folder migrations. migrate digunakan untuk menerapkan instruksi yang ada pada folder migrations ke dalam database dengan menerjemahkan file blueprint tadi menjadi SQL

### Tugas 3

1. Penggunaan ModelForm membuat html yang tadinya manual untuk setiap input, sedangkan dengan penggunaan ModelForm membuat validasi dan atribut field model tidak perlu dibuat satu per satu, ModelForm juga dapat langsung mengkonversi input menjadi instance model lalu tersimpan langsung ke database dengan menggunakan form.save. Wajib menambahkan csrf token karena penggunaan csrf akan menghasilkan elemen dengan input type yang hidden yang berisi token acak unk per sesi, jika token yang dikirimkan tidak cocok dengan token sesi pengguna, django akan menolak request tersebut.

2. Karena JSON hanya perlu menggunakan sintaks pasangan key-value sederhana seperti {"title": "Backend"}, sedangkan XML menggunakan tag pembuka dan penutup seperti <interest><title>Backend</title></interest>, JSON juga langsung dibaca karena JSON adalah bagian dari standar sintaks JS, sedangkan XML membutuhkan parser dokumen XML. Struktur data dengan JSON juga lebih bersih dan mudah dibaca dan lebih readable.

3. Alur pengembalian data JSON adalah mukai dari HTTP req diterima, ORM dieksekusi oleh View untuk mengambil data dari database.  Data yang sudah diambil melewati modul serializer django yang mengubah objek model Python menjadi string berformat JSON. Strin JSON tersebut dibungkus ke dalam objek JsonResponse. Server mengembalikan respon ke client dan kemudian diproses oleh frontend atau client API. Proses serialization diperlukan karena objek model django tidak bisa diterjemahkan langsung karena memiliki memori, metode, dan tipe data khusus seperti UUIDField dan DateTimeField.

### Tugas 5

1. Debouncing adalah teknik yang menunda eksekusi sebuah fungsi dengan jeda waktu ertentu sehingga mencegah request ke server pada setiap ketikan, misal ingin mengetik "ikan", tanpa debouncing, jika menggunakan fituer pencarian berbasis AJAX, maka setiap i, ik, ika, ikan, akan menjalankan request berturut turut

2. Fungsi await digunakan untuk menghentikan sementara eksekusi kode di dalam fungsi asynchronous hingga sebuah Promise selesai (resolved atau rejected) dan mengembalikan nilainya. Karena fetch() adalah operasi asynchronous yang mengembalikan objek Promise, kita memerlukan await agar program menunggu proses penarikan data dari server selesai, lalu mengembalikan objek Response yang utuh.

Jika tidak menggunakan await, eksekusi kode akan langsung berlanjut ke baris berikutnya tanpa menunggu respon server. Variabel yang menampung pemanggilan fetch() hanya akan berisi objek Promise dengan status pending (belum selesai), bukan data yang kita inginkan. Akibatnya, saat baris kode selanjutnya mencoba membaca atau memanipulasi data tersebut (misalnya dengan metode .json()), akan terjadi error karena datanya secara aktual belum tersedia di memori browser.

3. XSS (Cross-Site Scripting) adalah celah keamanan di mana penyerang berhasil menyuntikkan skrip berbahaya (biasanya JavaScript) ke dalam halaman web yang sah. Saat pengguna lain membuka halaman tersebut, browser mereka akan mengeksekusi skrip berbahaya tersebut, yang dapat berujung pada pencurian cookies/session token atau manipulasi halaman (phishing).Template Django memiliki perlindungan auto-escaping secara bawaan (default). Jika ada variabel berisi <script>alert(1)</script>, Django otomatis mengubahnya menjadi entitas HTML aman (&lt;script&gt;...) sebelum dikirim ke browser. Browser hanya akan membacanya sebagai teks biasa, bukan kode yang bisa dieksekusi. Sedangkan, AJAX/JavaScript umumnya menerima data mentah (misalnya format JSON) tanpa melalui filter auto-escaping dari sisi server. Saat developer menggunakan JavaScript untuk memanipulasi DOM dan memasukkan data tersebut menggunakan properti seperti innerHTML, tidak ada perlindungan bawaan. Jika JSON tersebut mengandung tag <script> atau atribut berbahaya (seperti <img src="x" onerror="alert(1)">), browser akan langsung mengeksekusinya. Untuk mengamankannya, developer harus secara manual menggunakan fungsi sanitasi (seperti DOMPurify) atau menggunakan properti yang aman dari eksekusi HTML, seperti textContent atau innerText. 

### Tugas 6

1. REST itu gaya arsitektur buat ngerancang web API, bukan library atau format data. Di REST, data dianggap sebagai resource yang ditunjuk lewat URL, misalnya `/api/v1/interests/` buat kumpulan minat dan `/api/v1/interests/<uuid>/` buat satu minat, terus tindakannya ditentukan sama HTTP method (GET buat baca, POST buat bikin, PUT/PATCH buat ubah, DELETE buat hapus), dan klien sama server tukeran representasi data dalam bentuk JSON. Jadi ngembaliin JSON aja belum cukup, contohnya di Tutorial 05 endpoint nya masih kayak `/projects/add-ajax/` atau `/projects/<uuid>/delete/` yang tindakannya ditulis di URL dan semuanya pakai POST, padahal responnya udah JSON. Yang bikin API itu RESTful adalah kontraknya konsisten: URL nunjuk resource, method nunjuk tindakan, dan status code nya sesuai (201, 400, 403, 404, 204). Untuk PUT, kita ngirim representasi lengkap buat ngegantiin data lama, jadi semua field wajib harus dikirim, kalau cuma kirim title doang bakal dapet 400. Sedangkan PATCH cuma ngirim field yang mau diubah, field lain tetap pakai nilai lama. PUT cocok dipakai kalau form edit nya ngirim ulang semua field (title, skill, image) sekaligus, sedangkan PATCH cocok kalau cuma mau ganti satu hal, misalnya Editor cuma mau benerin typo di title minat tanpa nyentuh skill dan gambarnya, kayak modal edit di halaman interest yang ngirim PATCH.

2. Serializer itu penghubung antara objek model Django dan data JSON, dan kerjanya dua arah. Pas GET, serializer ngubah objek Interest jadi tipe data Python yang bisa dirender ke JSON, dan pas POST/PUT/PATCH, serializer ngubah input dari klien jadi data yang udah divalidasi dan siap disimpan. Bedanya sama Tutorial 05, dulu di `get_interests_json` aku harus nyusun dictionary satu per satu di dalam perulangan, terus validasinya lewat form dan error nya juga dirakit manual pakai `form.errors.get_json_data()`. Kalau pakai serializer, daftar field cukup ditulis sekali di `Meta.fields`, field hitungan kayak `star_count` dan `is_starred` tinggal pakai `SerializerMethodField` yang otomatis read-only, validasi kayak `validate_title` juga ada di tempat yang sama, dan tinggal panggil `is_valid(raise_exception=True)` buat dapet respon 400 lengkap sama error per field. Selain itu karena field nya ditulis eksplisit, data sensitif kayak email atau password user yang ngasih star ga bakal ikut kebocor, dan kalau nanti bagian lain kayak Experience butuh API juga, polanya tinggal dipakai ulang.

3. Autentikasi itu ngejawab "siapa kamu", sedangkan otorisasi ngejawab "kamu boleh ngapain". Di DRF keduanya dipisah: authentication class kayak `SessionAuthentication` ngisi `request.user` dari session login, terus permission class kayak `IsPortfolioOwnerOrEditorOrReadOnly` yang mutusin request nya boleh lanjut atau ngga, misalnya Editor cuma boleh PUT/PATCH tapi ga boleh POST atau DELETE. Hak akses harus dicek di server karena nyembunyiin tombol di template cuma ngatur tampilan aja. Orang tetap bisa ngirim request langsung ke endpoint API, misalnya lewat Console di DevTools, Postman, atau curl, tanpa pernah liat tombolnya. Kalau server nya ga ngecek, user biasa bisa aja ngehapus data portofolio cuma dengan ngirim DELETE ke `/api/v1/interests/<uuid>/`. Makanya di test aku juga ngecek kalau user biasa dan Editor yang nyoba DELETE dapet 403 dan data di database nya beneran ga berubah.

4. `SessionAuthentication` ngenalin user dari cookie session, dan browser otomatis ngirim cookie itu di setiap request ke domain kita, termasuk request yang dipicu dari website lain. Jadi kalau ga ada token CSRF, website jahat bisa bikin browser user yang lagi login ngirim POST atau DELETE ke API kita, dan server bakal ngira itu request asli dari user tersebut. Token CSRF ngebuktiin kalau request nya beneran berasal dari halaman kita sendiri, karena website lain ga bisa baca cookie `csrftoken` kita, makanya di `fetch()` aku kirim header `X-CSRFToken` yang diambil dari `getCookie('csrftoken')`. Sedangkan `force_authenticate` di test langsung nganggap request sebagai user tertentu tanpa lewat proses login dan session yang beneran, jadi pengecekan CSRF nya juga ikut kelewat. Artinya test yang pakai `force_authenticate` cuma bisa buktiin permission nya bener, bukan buktiin CSRF nya jalan. Makanya perlu test pakai `APIClient(enforce_csrf_checks=True)` dan `.login()` yang bikin session asli, satu buat buktiin POST tanpa token ditolak dengan 403, dan satu lagi buat buktiin POST dengan token berhasil dengan 201.
