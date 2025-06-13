# todo_app/main.py
import tkinter as tk
from tkinter import messagebox
from core.task_manager import TaskManager

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi To-Do List")
        master.geometry("400x500")

        self.task_manager = TaskManager()

        # --- GUI Elements ---
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.task_input = tk.Entry(self.frame, width=40)
        self.task_input.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.frame, text="Tambah Tugas", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.task_list_frame = tk.Frame(master)
        self.task_list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.task_list = tk.Listbox(self.task_list_frame, width=50, height=15)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.task_list.bind("<<ListboxSelect>>", self.on_task_select)

        self.scrollbar = tk.Scrollbar(self.task_list_frame, orient="vertical")
        self.scrollbar.config(command=self.task_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.task_list.config(yscrollcommand=self.scrollbar.set)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.mark_complete_button = tk.Button(self.button_frame, text="Tandai Selesai", command=self.mark_task_complete, state=tk.DISABLED)
        self.mark_complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Hapus Tugas", command=self.delete_task, state=tk.DISABLED)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)
        tasks = self.task_manager.get_all_tasks()
        for i, task in enumerate(tasks):
            status = "✓ " if task['completed'] else "  "
            self.task_list.insert(tk.END, f"{status}{task['description']}")
            if task['completed']:
                self.task_list.itemconfig(i, {'fg': 'gray', 'bg': '#e0e0e0'})
            else:
                self.task_list.itemconfig(i, {'fg': 'black', 'bg': 'white'})
        self.update_buttons_state()

    def add_task(self):
        description = self.task_input.get().strip()
        if description:
            self.task_manager.add_task(description)
            self.task_input.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Input Kosong", "Deskripsi tugas tidak boleh kosong.")

    def on_task_select(self, event):
        self.update_buttons_state()

    def update_buttons_state(self):
        selected_indices = self.task_list.curselection()
        if selected_indices:
            self.mark_complete_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.mark_complete_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def get_selected_task_id(self):
        selected_indices = self.task_list.curselection()
        if selected_indices:
            index = selected_indices[0]
            tasks = self.task_manager.get_all_tasks()
            return tasks[index]['id']
        return None

    def mark_task_complete(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            if self.task_manager.mark_task_complete(task_id):
                self.refresh_tasks()
            else:
                messagebox.showerror("Error", "Gagal menandai tugas selesai.")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin ditandai selesai.")

    def delete_task(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            if messagebox.askyesno("Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus tugas ini?"):
                if self.task_manager.delete_task(task_id):
                    self.refresh_tasks()
                else:
                    messagebox.showerror("Error", "Gagal menghapus tugas.")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
