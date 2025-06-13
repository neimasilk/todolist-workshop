# Langkah 1: Setup Dasar Aplikasi dan Tampilan Menu

**Tujuan:** Membuat struktur file dan folder dasar untuk aplikasi serta mengimplementasikan loop utama yang menampilkan menu kepada pengguna.

**Petunjuk untuk AI Koding:**

1.  **Buat Struktur Folder dan File:**
    Buat struktur direktori dan file berikut di root proyek:

    ```
    .
    ├── .gitignore
    ├── todo_app/
    │   ├── core/
    │   │   └── __init__.py
    │   └── main.py
    └── requirements.txt
    ```

2.  **Isi File `.gitignore`:**
    Masukkan konten standar Python ke dalam file `.gitignore` untuk mengabaikan file yang tidak perlu.

    ```gitignore
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.pyc
    * .pyo
    * .pyd

    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    VENV/

    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    ```

3.  **Isi File `requirements.txt`:**
    Biarkan file ini kosong untuk saat ini. Kita akan menambahkannya nanti jika ada dependensi.

4.  **Isi File `todo_app/core/__init__.py`:**
    Biarkan file ini kosong. Keberadaannya menjadikan direktori `core` sebagai sebuah Python package.

5.  **Isi File `todo_app/main.py`:**
    Tulis kode Python berikut. Kode ini akan menjalankan loop utama aplikasi.

    ```python
    def main():
        """
        Fungsi utama untuk menjalankan aplikasi To-Do List.
        """
        while True:
            # Menampilkan pesan selamat datang dan menu
            print("\n--- Selamat Datang di Aplikasi To-Do List ---")
            print("1. Tambah Tugas")
            print("2. Lihat Tugas")
            print("3. Keluar")

            # Meminta input dari pengguna
            pilihan = input("Masukkan pilihan Anda (1/2/3): ")

            if pilihan == '1':
                # Fungsi untuk menambah tugas akan ditambahkan di langkah selanjutnya
                pass
            elif pilihan == '2':
                # Fungsi untuk melihat tugas akan ditambahkan di langkah selanjutnya
                pass
            elif pilihan == '3':
                # Keluar dari aplikasi
                print("Terima kasih telah menggunakan aplikasi To-Do List!")
                break
            else:
                # Opsi ini belum di-handle secara spesifik sesuai rencana,
                # jadi kita biarkan loop berlanjut untuk saat ini.
                pass

    if __name__ == "__main__":
        main()
    ```

**Verifikasi:**
Setelah kamu selesai, saya harus bisa menjalankan `python todo_app/main.py` dari terminal. Aplikasi harus menampilkan menu, dan jika saya mengetik `3` lalu menekan Enter, aplikasi harus mencetak pesan perpisahan dan berhenti.