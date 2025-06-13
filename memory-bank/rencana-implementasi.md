# Rencana Implementasi: Aplikasi To-Do List GUI

Dokumen ini menguraikan rencana implementasi untuk Aplikasi To-Do List versi GUI dengan penyimpanan data persisten, sebagaimana didefinisikan dalam `dokumen-desain-produk.md`.

## Tujuan

Menghasilkan aplikasi GUI fungsional yang memungkinkan pengguna untuk:
1.  Menambah tugas baru.
2.  Melihat semua tugas yang ada (dengan status selesai/belum selesai).
3.  Menandai tugas sebagai selesai.
4.  Menghapus tugas.
5.  Menyimpan dan memuat tugas secara persisten dari file JSON.

## Struktur Proyek

Struktur proyek yang digunakan adalah sebagai berikut:

```
todo_app/
├── app.py            # Titik masuk utama aplikasi, logika GUI Tkinter
└── core/
    ├── __init__.py
    └── task_manager.py # Kelas/modul untuk mengelola tugas (tambah, lihat, tandai selesai, hapus, muat, simpan)
└── data/
    └── tasks.json    # File JSON untuk penyimpanan data persisten
```

## Langkah-Langkah Implementasi

Berikut adalah pemecahan fitur menjadi langkah-langkah yang lebih kecil dan dapat dikelola. Setiap langkah memiliki kriteria keberhasilan yang jelas.

### Langkah 1: Penyiapan Struktur Proyek dan File Data

*   **Deskripsi:** Membuat struktur folder dasar dan file `tasks.json` untuk penyimpanan persisten.
*   **Tugas:**
    *   Buat folder `todo_app/`.
    *   Buat folder `todo_app/core/`.
    *   Buat file `todo_app/core/__init__.py`.
    *   Buat folder `todo_app/data/`.
    *   Buat file `todo_app/data/tasks.json` dengan konten `[]` (array kosong JSON).
*   **Kriteria Keberhasilan:**
    *   Struktur folder dan file yang disebutkan di atas telah dibuat.
    *   `tasks.json` ada dan berisi array JSON kosong.

### Langkah 2: Refaktor `TaskManager` untuk Fitur Lengkap dan Persistensi

*   **Deskripsi:** Memperbarui kelas `TaskManager` untuk mengelola tugas sebagai objek (dengan ID, deskripsi, dan status selesai) serta menambahkan fungsionalitas muat/simpan data.
*   **Tugas (dalam `task_manager.py`):**
    *   Impor modul `json` dan `os`.
    *   Inisialisasi `self.file_path` ke `todo_app/data/tasks.json`.
    *   Implementasikan `load_tasks()` untuk membaca tugas dari `tasks.json`.
    *   Implementasikan `save_tasks()` untuk menulis tugas ke `tasks.json`.
    *   Modifikasi `__init__` untuk memuat tugas saat inisialisasi dan menetapkan `next_id`.
    *   Modifikasi `add_task` untuk membuat objek tugas dengan ID unik dan status `completed: False`, lalu menyimpannya.
    *   Implementasikan `mark_task_complete(task_id)` untuk mengubah status `completed` tugas.
    *   Implementasikan `delete_task(task_id)` untuk menghapus tugas berdasarkan ID.
*   **Kriteria Keberhasilan:**
    *   `TaskManager` dapat memuat dan menyimpan tugas ke/dari `tasks.json`.
    *   `add_task` membuat tugas dengan ID dan status yang benar.
    *   `mark_task_complete` dan `delete_task` berfungsi dengan benar dan memperbarui file JSON.

### Langkah 3: Mengembangkan Antarmuka GUI dengan Tkinter di `app.py`

*   **Deskripsi:** Membuat antarmuka pengguna grafis menggunakan Tkinter untuk berinteraksi dengan `TaskManager`.
*   **Tugas (dalam `app.py`):**
    *   Impor `tkinter` dan `messagebox`, serta `TaskManager`.
    *   Buat kelas `TodoApp` yang mengelola GUI.
    *   Dalam `__init__` `TodoApp`:
        *   Inisialisasi jendela utama Tkinter (`master`).
        *   Buat instance `TaskManager`.
        *   Buat elemen GUI: `Entry` untuk input tugas, `Button` untuk tambah, `Listbox` untuk menampilkan tugas, `Scrollbar`, dan tombol "Tandai Selesai" serta "Hapus Tugas".
        *   Atur tata letak elemen menggunakan `pack()`.
        *   Hubungkan tombol ke metode yang sesuai (`add_task`, `mark_task_complete`, `delete_task`).
        *   Hubungkan event `<<ListboxSelect>>` untuk mengaktifkan/menonaktifkan tombol.
    *   Implementasikan `refresh_tasks()` untuk memperbarui `Listbox` dengan tugas-tugas dari `TaskManager`, termasuk indikator status selesai.
    *   Implementasikan `add_task()` untuk mengambil input, memanggil `task_manager.add_task()`, dan me-refresh GUI.
    *   Implementasikan `mark_task_complete()` dan `delete_task()` untuk mendapatkan ID tugas yang dipilih, memanggil metode `TaskManager` yang sesuai, dan me-refresh GUI.
    *   Implementasikan `on_task_select()` dan `update_buttons_state()` untuk mengelola status tombol berdasarkan pilihan di `Listbox`.
    *   Buat fungsi `main()` untuk menjalankan aplikasi Tkinter.
*   **Kriteria Keberhasilan:**
    *   Aplikasi GUI terbuka dengan benar.
    *   Elemen GUI ditampilkan dengan tata letak yang benar.
    *   Pengguna dapat menambah tugas, melihatnya di daftar, menandainya selesai, dan menghapusnya melalui GUI.
    *   Data tugas disimpan dan dimuat secara persisten.

## Pengujian dan Validasi

*   Setiap fungsionalitas GUI akan diuji secara manual untuk memastikan interaksi yang benar.
*   Pengujian persistensi data akan dilakukan dengan menutup dan membuka kembali aplikasi untuk memverifikasi bahwa tugas-tugas tersimpan.
*   Kriteria keberhasilan yang tercantum di `dokumen-desain-produk.md` harus terpenuhi.

Dokumen ini akan menjadi dasar untuk pengembangan lebih lanjut.
