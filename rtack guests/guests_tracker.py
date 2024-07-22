import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database connection
conn = sqlite3.connect('guests.db')
c = conn.cursor()

# Create a table to store guest information if not exists
c.execute('''CREATE TABLE IF NOT EXISTS guests (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER,
             email TEXT NOT NULL UNIQUE,
             rsvp_status TEXT
             )''')
conn.commit()

# Function to add guest information to the database
def add_guest():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    
    # Check if the email is already in the database
    c.execute("SELECT * FROM guests WHERE email=?", (email,))
    if c.fetchone():
        messagebox.showerror("Error", "Email already registered!")
        return

    # Add guest to the database
    c.execute("INSERT INTO guests (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    messagebox.showinfo("Success", "Guest added successfully!")

    # Clear the entry fields after adding
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to search for a guest by email
def search_guest():
    email = entry_search_email.get()
    c.execute("SELECT * FROM guests WHERE email=?", (email,))
    guest = c.fetchone()

    if guest:
        name, age, email, rsvp_status = guest
        messagebox.showinfo("Guest Found", f"Name: {name}\nAge: {age}\nEmail: {email}\nRSVP Status: {rsvp_status}")
    else:
        messagebox.showerror("Error", "Guest not found!")

    entry_search_email.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Wedding Guests Verification Program")

# Add Guest Frame
frame_add_guest = tk.Frame(root)
frame_add_guest.pack(padx=10, pady=10)

label_name = tk.Label(frame_add_guest, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_add_guest)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_age = tk.Label(frame_add_guest, text="Age:")
label_age.grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(frame_add_guest)
entry_age.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(frame_add_guest, text="Email:")
label_email.grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_add_guest)
entry_email.grid(row=2, column=1, padx=5, pady=5)

button_add_guest = tk.Button(frame_add_guest, text="Add Guest", command=add_guest)
button_add_guest.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Search Guest Frame
frame_search_guest = tk.Frame(root)
frame_search_guest.pack(padx=10, pady=10)

label_search_email = tk.Label(frame_search_guest, text="Search by Email:")
label_search_email.grid(row=0, column=0, padx=5, pady=5)
entry_search_email = tk.Entry(frame_search_guest)
entry_search_email.grid(row=0, column=1, padx=5, pady=5)

button_search_guest = tk.Button(frame_search_guest, text="Search", command=search_guest)
button_search_guest.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI main loop
root.mainloop()

# Close the database connection when the GUI is closed
conn.close()
