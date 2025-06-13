# Arsitektur Aplikasi To-Do List GUI

Dokumen ini menjelaskan arsitektur tingkat tinggi dari Aplikasi To-Do List berbasis GUI.

## 1. Gambaran Umum Arsitektur

Aplikasi ini mengadopsi arsitektur modular sederhana yang memisahkan logika bisnis (manajemen tugas) dari antarmuka pengguna (GUI). Ini memungkinkan fleksibilitas untuk mengubah atau memperluas salah satu bagian tanpa mempengaruhi yang lain secara drastis.

```mermaid
graph TD
    A[Pengguna] --> B[Antarmuka Pengguna (GUI - Tkinter)]
    B --> C[Logika Aplikasi (app.py)]
    C --> D[Manajer Tugas (TaskManager)]
    D --> E[Penyimpanan Data (tasks.json)]
    E --> D
    D --> C
    C --> B
```

## 2. Komponen Utama

### 2.1. Antarmuka Pengguna (GUI - Tkinter)

*   **Lokasi:** `todo_app/app.py`
*   **Deskripsi:** Bertanggung jawab untuk semua interaksi visual dengan pengguna. Ini mencakup tampilan daftar tugas, kolom input untuk tugas baru, dan tombol-tombol untuk menambah, menandai selesai, dan menghapus tugas.
*   **Teknologi:** Tkinter (pustaka GUI standar Python).
*   **Interaksi:** Menerima input dari pengguna (misalnya, teks tugas, klik tombol) dan menampilkan informasi yang relevan (daftar tugas yang diperbarui, status tugas).

### 2.2. Logika Aplikasi (`app.py`)

*   **Lokasi:** `todo_app/app.py`
*   **Deskripsi:** Bertindak sebagai "controller" yang menghubungkan GUI dengan logika manajemen tugas. Ini menginisialisasi aplikasi GUI dan `TaskManager`, serta menerjemahkan aksi pengguna dari GUI menjadi panggilan metode pada `TaskManager`.
*   **Tanggung Jawab:**
    *   Membuat dan mengelola jendela utama Tkinter.
    *   Membuat instance `TaskManager`.
    *   Menangani event GUI (misalnya, klik tombol, pemilihan item listbox).
    *   Memanggil metode yang sesuai di `TaskManager` berdasarkan aksi pengguna.
    *   Memperbarui tampilan GUI berdasarkan data yang diterima dari `TaskManager`.

### 2.3. Manajer Tugas (`TaskManager`)

*   **Lokasi:** `todo_app/core/task_manager.py`
*   **Deskripsi:** Merupakan inti logika bisnis aplikasi. Bertanggung jawab untuk semua operasi terkait tugas, seperti menambah, melihat, menandai selesai, menghapus, serta memuat dan menyimpan data tugas.
*   **Tanggung Jawab:**
    *   Mengelola koleksi tugas (dalam memori).
    *   Menyediakan API untuk operasi CRUD (Create, Read, Update, Delete) pada tugas.
    *   Berinteraksi langsung dengan sistem penyimpanan data (file JSON).
    *   Menjaga konsistensi data.

### 2.4. Penyimpanan Data (`tasks.json`)

*   **Lokasi:** `todo_app/data/tasks.json`
*   **Deskripsi:** File ini digunakan untuk menyimpan data tugas secara persisten dalam format JSON. Ini memastikan bahwa data tugas tidak hilang ketika aplikasi ditutup.
*   **Teknologi:** JSON (JavaScript Object Notation).
*   **Interaksi:** `TaskManager` membaca dari dan menulis ke file ini.

## 3. Alur Data

1.  **Aplikasi Dimulai:** `app.py` menginisialisasi `TodoApp`, yang kemudian membuat instance `TaskManager`. `TaskManager` memuat tugas dari `tasks.json`.
2.  **Tambah Tugas:** Pengguna memasukkan teks di GUI (`app.py`), `app.py` memanggil `add_task` di `TaskManager`. `TaskManager` menambahkan tugas ke daftar internalnya dan memanggil `save_tasks` untuk memperbarui `tasks.json`. `app.py` kemudian me-refresh tampilan GUI.
3.  **Lihat Tugas:** `app.py` memanggil `get_all_tasks` di `TaskManager`. `TaskManager` mengembalikan daftar tugas, yang kemudian ditampilkan oleh GUI di `app.py`.
4.  **Tandai Selesai/Hapus Tugas:** Pengguna memilih tugas di GUI (`app.py`), `app.py` mendapatkan ID tugas dan memanggil `mark_task_complete` atau `delete_task` di `TaskManager`. `TaskManager` memodifikasi daftar internalnya dan memanggil `save_tasks`. `app.py` kemudian me-refresh tampilan GUI.
5.  **Aplikasi Ditutup:** `app.py` berhenti, dan karena `save_tasks` dipanggil setelah setiap modifikasi, data sudah tersimpan.

Arsitektur ini mempromosikan pemisahan kekhawatiran (separation of concerns), membuat kode lebih mudah dipelihara, diuji, dan diperluas.
