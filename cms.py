import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE = "C:\\Users\\lenovo\\Documents\\Contact.csv"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    contact_list.insert(tk.END, line)

def save_contacts():
    contacts = contact_list.get(0, tk.END)
    with open(FILE, 'w') as f:
        for contact in contacts:
            f.write(contact + "\n")

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contact = f"{name} | {phone} | {email}"
        contact_list.insert(tk.END, contact)
        save_contacts()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please fill all fields")

def delete_contact():
    try:
        selected = contact_list.curselection()[0]
        contact_list.delete(selected)
        save_contacts()
    except IndexError:
        messagebox.showwarning("Error", "Select a contact to delete")

# GUI setup
root = tk.Tk()
root.title("Simple Contact Manager")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Phone").grid(row=1, column=0)
tk.Label(root, text="Email").grid(row=2, column=0)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)

add_btn = tk.Button(root, text="Add", command=add_contact)
add_btn.grid(row=3, column=0, columnspan=2, sticky="we")

delete_btn = tk.Button(root, text="Delete", command=delete_contact)
delete_btn.grid(row=4, column=0, columnspan=2, sticky="we")

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=5, column=0, columnspan=2)

load_contacts()

root.mainloop()