# todo_app/main.py

from core.task_manager import TaskManager

def display_menu():
    print("\nDaftar Perintah:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Keluar")

def main():
    print("Selamat datang di Aplikasi To-Do List CLI!")
    task_manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("Masukkan pilihan Anda: ").strip()

        if choice == '1':
            description = input("Masukkan deskripsi tugas baru: ").strip()
            if description:
                task_manager.add_task(description)
                print(f"Tugas '{description}' telah ditambahkan.")
            else:
                print("Deskripsi tugas tidak boleh kosong.")
        elif choice == '2':
            tasks = task_manager.get_all_tasks()
            if tasks:
                print("\nDaftar Tugas:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("Tidak ada tugas saat ini.")
        elif choice == '3':
            print("Terima kasih telah menggunakan aplikasi To-Do List!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()
