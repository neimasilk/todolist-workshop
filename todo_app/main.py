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