import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#f2f4f7")

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 18),
            bd=5,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="x", padx=10, pady=10)

        btn_frame = tk.Frame(root, bg="#f2f4f7")
        btn_frame.pack()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0

        for btn in buttons:
            action = lambda x=btn: self.on_click(x)
            tk.Button(
                btn_frame,
                text=btn,
                width=5,
                height=2,
                font=("Arial", 14),
                command=action
            ).grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(
            root,
            text="Clear",
            width=20,
            height=2,
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            command=self.clear
        ).pack(pady=10)

    def on_click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear()
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
