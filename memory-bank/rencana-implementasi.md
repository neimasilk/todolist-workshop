# Rencana Implementasi: MVP Aplikasi To-Do List (Web-Based)

Dokumen ini menguraikan rencana implementasi untuk *Minimum Viable Product* (MVP) dari Aplikasi To-Do List versi Web-Based, sebagai evolusi dari rencana CLI yang didefinisikan dalam `proposal.md` dan `dokumen-desain-produk.md`.

## Tujuan MVP

Menghasilkan aplikasi web fungsional yang memungkinkan pengguna untuk:
1.  Menambah tugas baru melalui antarmuka web.
2.  Melihat semua tugas yang ada dalam tampilan web yang responsif.
3.  Menandai tugas sebagai selesai.
4.  Menghapus tugas.
5.  Menyimpan data secara persisten.

Data tugas akan disimpan dalam database SQLite untuk persistensi data.

## Struktur Proyek Web-Based (Saran)

Struktur proyek untuk aplikasi web menggunakan Flask:

```
todo_app/
├── app.py              # Aplikasi Flask utama
├── models.py           # Model database untuk tugas
├── static/
│   ├── css/
│   │   └── style.css   # Styling untuk antarmuka web
│   └── js/
│       └── main.js     # JavaScript untuk interaktivitas
├── templates/
│   ├── base.html       # Template dasar
│   └── index.html      # Halaman utama aplikasi
└── database.db         # Database SQLite (akan dibuat otomatis)
memory-bank/
├── proposal.md
├── dokumen-desain-produk.md
├── tumpukan-teknologi.md
└── rencana-implementasi.md
└── ... (file lainnya)
requirements.txt        # Dependencies Python
README.md
```

Struktur ini mengikuti pola MVC (Model-View-Controller) yang umum untuk aplikasi web Flask.

## Langkah-Langkah Implementasi MVP Web-Based

Berikut adalah pemecahan fitur MVP menjadi langkah-langkah yang lebih kecil dan dapat dikelola. Setiap langkah harus memiliki kriteria keberhasilan yang jelas.

### Langkah 1: Setup Dasar Aplikasi Flask dan Struktur Folder

*   **Deskripsi:** Membuat struktur folder dasar dan aplikasi Flask minimal.
*   **Tugas:**
    *   Buat folder `todo_app/`.
    *   Buat file `todo_app/app.py` sebagai aplikasi Flask utama.
    *   Buat folder `todo_app/templates/` untuk template HTML.
    *   Buat folder `todo_app/static/` dengan subfolder `css/` dan `js/`.
    *   Buat file `requirements.txt` dengan dependencies Flask dan SQLAlchemy.
    *   Implementasikan aplikasi Flask dasar dengan route utama.
*   **Kriteria Keberhasilan:**
    *   Server Flask dapat dijalankan (`python todo_app/app.py`).
    *   Aplikasi dapat diakses melalui browser di `http://localhost:5000`.
    *   Halaman utama menampilkan pesan selamat datang.
    *   Tidak ada error saat menjalankan server.

### Langkah 2: Implementasi Model Database dan Fungsionalitas Dasar

*   **Deskripsi:** Membuat model database untuk tugas dan implementasi CRUD dasar.
*   **Tugas:**
    *   Buat file `todo_app/models.py` dengan model Task menggunakan SQLAlchemy.
    *   Implementasikan database SQLite dengan tabel tasks.
    *   Buat fungsi untuk inisialisasi database.
    *   Implementasikan fungsi CRUD dasar (Create, Read, Update, Delete).
*   **Kriteria Keberhasilan:**
    *   Database SQLite terbuat otomatis saat aplikasi dijalankan.
    *   Model Task dapat menyimpan id, deskripsi, status selesai, dan timestamp.
    *   Fungsi CRUD dapat diuji melalui Python shell.
    *   Tidak ada error database saat aplikasi dijalankan.

### Langkah 3: Implementasi Template HTML dan Antarmuka Dasar

*   **Deskripsi:** Membuat template HTML untuk menampilkan dan mengelola tugas.
*   **Tugas:**
    *   Buat file `todo_app/templates/base.html` sebagai template dasar.
    *   Buat file `todo_app/templates/index.html` untuk halaman utama.
    *   Implementasikan form untuk menambah tugas baru.
    *   Implementasikan tampilan daftar tugas dengan opsi edit dan hapus.
    *   Tambahkan CSS dasar untuk styling yang menarik.
*   **Kriteria Keberhasilan:**
    *   Halaman utama menampilkan form input tugas dan daftar tugas.
    *   Form dapat digunakan untuk menambah tugas baru.
    *   Daftar tugas menampilkan semua tugas dengan status yang jelas.
    *   Tampilan responsif dan user-friendly.

### Langkah 4: Implementasi Fungsionalitas CRUD Lengkap

*   **Deskripsi:** Mengimplementasikan semua operasi CRUD melalui antarmuka web.
*   **Tugas:**
    *   Implementasikan route Flask untuk menambah tugas (POST).
    *   Implementasikan route untuk menandai tugas selesai/belum selesai (PUT).
    *   Implementasikan route untuk menghapus tugas (DELETE).
    *   Tambahkan JavaScript untuk interaksi AJAX yang smooth.
    *   Implementasikan validasi form dan error handling.
*   **Kriteria Keberhasilan:**
    *   Pengguna dapat menambah tugas baru melalui form web.
    *   Pengguna dapat menandai tugas sebagai selesai/belum selesai.
    *   Pengguna dapat menghapus tugas.
    *   Semua operasi berjalan tanpa refresh halaman (AJAX).
    *   Validasi input berfungsi dengan baik.

### Langkah 5: Styling dan User Experience Enhancement

*   **Deskripsi:** Meningkatkan tampilan dan pengalaman pengguna aplikasi web.
*   **Tugas:**
    *   Implementasikan CSS framework (Bootstrap atau custom CSS) untuk tampilan modern.
    *   Tambahkan animasi dan transisi untuk interaksi yang smooth.
    *   Implementasikan responsive design untuk mobile dan desktop.
    *   Tambahkan feedback visual untuk aksi pengguna (loading, success, error).
*   **Kriteria Keberhasilan:**
    *   Aplikasi memiliki tampilan modern dan menarik.
    *   Aplikasi responsif di berbagai ukuran layar.
    *   Interaksi pengguna memberikan feedback yang jelas.
    *   User experience yang intuitif dan mudah digunakan.

## Pengujian dan Validasi MVP

*   Setiap langkah di atas akan diuji secara manual dan otomatis selama pengembangan.
*   Pengujian akan mencakup functionality testing, usability testing, dan responsive design testing.
*   Pengujian akhir MVP akan melibatkan menjalankan semua fungsionalitas melalui browser untuk memastikan integrasi bekerja dengan baik.
*   Kriteria keberhasilan untuk MVP secara keseluruhan (seperti yang tercantum di `dokumen-desain-produk.md`) harus terpenuhi.

Dokumen ini akan menjadi dasar untuk pembuatan `baby-step.md` yang lebih detail untuk setiap langkah implementasi oleh AI Perencana (Gemini).
