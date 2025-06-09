import tkinter as tk
from tkinter import messagebox

# Function to add contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone and email:
        contact_listbox.insert(tk.END, f"{name} | {phone} | {email}")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to delete contact
def delete_contact():
    try:
        selected_contact = contact_listbox.curselection()
        contact_listbox.delete(selected_contact)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete")

# Function to search contact
def search_contact():
    search_term = entry_search.get().lower()
    for i in range(contact_listbox.size()):
        contact = contact_listbox.get(i).lower()
        if search_term in contact:
            contact_listbox.select_clear(0, tk.END)
            contact_listbox.selection_set(i)
            break
    else:
        messagebox.showinfo("Not Found", "No matching contact found!")

# Function to update contact
def update_contact():
    try:
        selected_contact = contact_listbox.curselection()
        old_contact = contact_listbox.get(selected_contact)

        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()

        if name and phone and email:
            new_contact = f"{name} | {phone} | {email}"
            contact_listbox.delete(selected_contact)
            contact_listbox.insert(selected_contact, new_contact)

            entry_name.delete(0, tk.END)
            entry_phone.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to update")

# GUI setup
root = tk.Tk()
root.title("Contact Management System")

# Labels and Entries
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0)

entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=0, columnspan=2)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=5, column=0, columnspan=2)

# Search Section
label_search = tk.Label(root, text="Search:")
label_search.grid(row=6, column=0)

entry_search = tk.Entry(root)
entry_search.grid(row=6, column=1)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=7, column=0, columnspan=2)

# Listbox for displaying contacts
contact_listbox = tk.Listbox(root, height=10, width=40)
contact_listbox.grid(row=8, column=0, columnspan=2)

# Run the GUI
root.mainloop()