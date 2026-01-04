import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.configure(bg="#f2f4f7")

        self.task_var = tk.StringVar()
        self.tasks = []

        tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#f2f4f7").pack(pady=10)

        entry_frame = tk.Frame(root, bg="#f2f4f7")
        entry_frame.pack(pady=5)

        tk.Entry(entry_frame, textvariable=self.task_var, width=30).grid(row=0, column=0, padx=5)
        tk.Button(entry_frame, text="Add", width=8, command=self.add_task, bg="#4caf50", fg="white").grid(row=0, column=1)

        self.listbox = tk.Listbox(root, width=45, height=15)
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#f2f4f7")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Delete", width=12, command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Clear All", width=12, command=self.clear_all).grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_var.get()
        if task == "":
            messagebox.showwarning("Warning", "Task cannot be empty")
            return
        self.tasks.append(task)
        self.listbox.insert(tk.END, task)
        self.task_var.set("")

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        index = selected[0]
        self.listbox.delete(index)
        self.tasks.pop(index)

    def clear_all(self):
        self.listbox.delete(0, tk.END)
        self.tasks.clear()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
