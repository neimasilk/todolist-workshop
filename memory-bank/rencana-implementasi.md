# Rencana Implementasi Awal: MVP Aplikasi To-Do List (CLI)

Dokumen ini menguraikan rencana implementasi untuk *Minimum Viable Product* (MVP) dari Aplikasi To-Do List versi CLI, sebagaimana didefinisikan dalam `proposal.md` dan `dokumen-desain-produk.md`.

## Tujuan MVP

Menghasilkan aplikasi CLI fungsional yang memungkinkan pengguna untuk:
1.  Menambah tugas baru.
2.  Melihat semua tugas yang ada.
3.  Keluar dari aplikasi.

Data tugas hanya akan tersimpan dalam memori selama aplikasi berjalan.

## Struktur Proyek Awal (Saran)

Meskipun MVP sangat sederhana, disarankan untuk memulai dengan struktur dasar yang dapat dikembangkan:

```
todo_app/
├── main.py           # Titik masuk utama aplikasi, logika CLI
└── core/
    ├── __init__.py
    └── task_manager.py # Kelas/modul untuk mengelola tugas (tambah, lihat)
memory-bank/
├── proposal.md
├── dokumen-desain-produk.md
├── tumpukan-teknologi.md
└── rencana-implementasi.md
└── ... (file lainnya)
README.md
```

Struktur ini bersifat saran dan dapat disesuaikan oleh AI Koding (Jules) berdasarkan `baby-step.md` yang lebih detail nantinya.

## Langkah-Langkah Implementasi MVP

Berikut adalah pemecahan fitur MVP menjadi langkah-langkah yang lebih kecil dan dapat dikelola. Setiap langkah harus memiliki kriteria keberhasilan yang jelas.

### Langkah 1: Setup Dasar Aplikasi dan Struktur Folder

*   **Deskripsi:** Membuat struktur folder dasar dan file `main.py` sebagai titik masuk aplikasi.
*   **Tugas:**
    *   Buat folder `todo_app/`.
    *   Buat file `todo_app/main.py`.
    *   Buat folder `todo_app/core/`.
    *   Buat file `todo_app/core/__init__.py`.
    *   Buat file `todo_app/core/task_manager.py`.
    *   Implementasikan loop utama aplikasi di `main.py` yang dapat menerima input pengguna dan menampilkan menu sederhana.
*   **Kriteria Keberhasilan:**
    *   Aplikasi dapat dijalankan (`python todo_app/main.py`).
    *   Aplikasi menampilkan pesan selamat datang dan opsi menu (misalnya, "1. Tambah Tugas", "2. Lihat Tugas", "3. Keluar").
    *   Aplikasi menunggu input pengguna.
    *   Memilih opsi "Keluar" akan menghentikan aplikasi dengan benar.

### Langkah 2: Implementasi Fungsionalitas "Tambah Tugas"

*   **Deskripsi:** Mengembangkan logika untuk menambahkan tugas baru ke dalam memori.
*   **Tugas (dalam `task_manager.py` dan dipanggil dari `main.py`):**
    *   Buat fungsi atau metode dalam `task_manager.py` untuk menyimpan tugas (misalnya, dalam sebuah list).
    *   Di `main.py`, saat pengguna memilih opsi "Tambah Tugas":
        *   Minta pengguna memasukkan deskripsi tugas.
        *   Panggil fungsi dari `task_manager.py` untuk menyimpan tugas tersebut.
        *   Tampilkan pesan konfirmasi.
*   **Kriteria Keberhasilan:**
    *   Pengguna dapat memasukkan deskripsi tugas.
    *   Tugas disimpan dalam struktur data internal (misalnya, list dalam `TaskManager`).
    *   Pesan konfirmasi "Tugas '[deskripsi]' telah ditambahkan." ditampilkan.

### Langkah 3: Implementasi Fungsionalitas "Lihat Tugas"

*   **Deskripsi:** Mengembangkan logika untuk menampilkan semua tugas yang tersimpan.
*   **Tugas (dalam `task_manager.py` dan dipanggil dari `main.py`):**
    *   Buat fungsi atau metode dalam `task_manager.py` untuk mengambil semua tugas yang tersimpan.
    *   Di `main.py`, saat pengguna memilih opsi "Lihat Tugas":
        *   Panggil fungsi dari `task_manager.py` untuk mendapatkan daftar tugas.
        *   Tampilkan tugas-tugas tersebut dalam format yang jelas (misalnya, dengan nomor urut).
        *   Jika tidak ada tugas, tampilkan pesan "Tidak ada tugas saat ini."
*   **Kriteria Keberhasilan:**
    *   Semua tugas yang telah ditambahkan ditampilkan dengan benar.
    *   Jika belum ada tugas, pesan yang sesuai akan ditampilkan.
    *   Format tampilan jelas dan mudah dibaca.

### Langkah 4: Penanganan Input Tidak Valid

*   **Deskripsi:** Memastikan aplikasi memberikan respons yang sesuai jika pengguna memasukkan opsi menu yang tidak valid.
*   **Tugas (dalam `main.py`):**
    *   Jika pengguna memasukkan input yang tidak sesuai dengan opsi menu yang tersedia (misalnya, bukan "1", "2", atau "3"), tampilkan pesan error.
    *   Tampilkan kembali daftar opsi menu yang valid.
*   **Kriteria Keberhasilan:**
    *   Aplikasi menampilkan pesan error yang informatif untuk input tidak valid.
    *   Aplikasi tidak crash dan kembali menampilkan menu.

## Pengujian dan Validasi MVP

*   Setiap langkah di atas akan diuji secara manual selama pengembangan awal.
*   Pengujian akhir MVP akan melibatkan menjalankan semua fungsionalitas secara berurutan untuk memastikan integrasi bekerja dengan baik.
*   Kriteria keberhasilan untuk MVP secara keseluruhan (seperti yang tercantum di `dokumen-desain-produk.md`) harus terpenuhi.

Dokumen ini akan menjadi dasar untuk pembuatan `baby-step.md` yang lebih detail untuk setiap langkah implementasi oleh AI Perencana (Gemini).
