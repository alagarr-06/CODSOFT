import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f2f4f7")

        self.length_var = tk.StringVar()
        self.result_var = tk.StringVar()

        tk.Label(
            root,
            text="Password Generator",
            font=("Arial", 16, "bold"),
            bg="#f2f4f7"
        ).pack(pady=10)

        frame = tk.Frame(root, bg="#f2f4f7")
        frame.pack(pady=10)

        tk.Label(frame, text="Password Length:", bg="#f2f4f7").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(frame, textvariable=self.length_var, width=15).grid(row=0, column=1, padx=5)

        tk.Button(
            root,
            text="Generate Password",
            width=20,
            bg="#4caf50",
            fg="white",
            command=self.generate_password
        ).pack(pady=10)

        tk.Entry(
            root,
            textvariable=self.result_var,
            width=35,
            font=("Arial", 12),
            justify="center"
        ).pack(pady=10)

        tk.Button(
            root,
            text="Clear",
            width=20,
            bg="#f44336",
            fg="white",
            command=self.clear
        ).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                raise ValueError

            chars = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(chars) for _ in range(length))
            self.result_var.set(password)

        except:
            messagebox.showerror("Error", "Please enter a valid positive number")

    def clear(self):
        self.length_var.set("")
        self.result_var.set("")

root = tk.Tk()
app = PasswordGenerator(root)
root.mainloop()
