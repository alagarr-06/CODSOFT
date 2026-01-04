import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x400")
        self.root.configure(bg="#f2f4f7")

        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        tk.Label(
            root,
            text="Contact Book",
            font=("Arial", 16, "bold"),
            bg="#f2f4f7"
        ).pack(pady=10)

        form = tk.Frame(root, bg="#f2f4f7")
        form.pack(pady=5)

        tk.Label(form, text="Name", bg="#f2f4f7").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(form, textvariable=self.name_var, width=25).grid(row=0, column=1)

        tk.Label(form, text="Phone", bg="#f2f4f7").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(form, textvariable=self.phone_var, width=25).grid(row=1, column=1)

        tk.Label(form, text="Email", bg="#f2f4f7").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(form, textvariable=self.email_var, width=25).grid(row=2, column=1)

        btn_frame = tk.Frame(root, bg="#f2f4f7")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add", width=10, bg="#4caf50", fg="white", command=self.add_contact).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", width=10, bg="#2196f3", fg="white", command=self.update_contact).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", width=10, bg="#f44336", fg="white", command=self.delete_contact).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Clear", width=10, command=self.clear_fields).grid(row=0, column=3, padx=5)

        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.select_contact)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()

        if name == "" or phone == "":
            messagebox.showwarning("Warning", "Name and Phone are required")
            return

        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.refresh_list()
        self.clear_fields()

    def update_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            return

        index = selected[0]
        self.contacts[index]["name"] = self.name_var.get()
        self.contacts[index]["phone"] = self.phone_var.get()
        self.contacts[index]["email"] = self.email_var.get()

        self.refresh_list()
        self.clear_fields()

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            return

        index = selected[0]
        self.contacts.pop(index)
        self.refresh_list()
        self.clear_fields()

    def select_contact(self, event):
        selected = self.listbox.curselection()
        if not selected:
            return

        contact = self.contacts[selected[0]]
        self.name_var.set(contact["name"])
        self.phone_var.set(contact["phone"])
        self.email_var.set(contact["email"])

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for c in self.contacts:
            self.listbox.insert(tk.END, f'{c["name"]} | {c["phone"]} | {c["email"]}')

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")

root = tk.Tk()
app = ContactBook(root)
root.mainloop()
