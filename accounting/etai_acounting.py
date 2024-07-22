import tkinter as tk
from tkinter import filedialog
import os
import shutil
import sqlite3
from datetime import datetime


font1 = "Tahoma"
size1 = 12
size2 = 18
size3 = 15
bg1 = "gray"
bg2 = "orange"
bg3 = "lightgreen"
fg1 = "white"
fg2 = "lightblue"

# Define a function to adapt datetime objects to SQLite
def adapt_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S").encode('utf-8')

# Register the adapter
sqlite3.register_adapter(datetime, adapt_datetime)

# Create SQLite database
conn = sqlite3.connect('finances.db')
c = conn.cursor()

# Create the table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (id INTEGER PRIMARY KEY,
             type TEXT,
             amount REAL,
             subject TEXT,
             file_path TEXT,
             folder_path TEXT,
             date_time TEXT)''')

# Create GUI
root = tk.Tk()
root.title("Etai Hatuel - Financials Tracker")
root.geometry("600x550+3+3")
root.config(bg=bg1)
# Functions
def update_listbox():
    transactions_listbox.delete(0, tk.END)
    # Fetch transaction records from the database
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    # Insert transaction data into the Listbox
    for transaction in transactions:
        transactions_listbox.insert(tk.END, f"{transaction[0]}: {transaction[1]} - {transaction[2]}")
        
def save_transaction():
    try:
        amount = float(amount_entry.get())
        subject = subject_entry.get()
        file_path = file_entry.get()
        if not file_path:
            file_path = "N/A"
        
        # Create folder
        folder_name = 'incomes' if amount >= 0 else 'expenses'
        folder_path = os.path.join(folder_name, f"{abs(amount)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        os.makedirs(folder_path)
        
        # Insert into database
        c.execute("INSERT INTO transactions (type, amount, subject, file_path, folder_path, date_time) VALUES (?, ?, ?, ?, ?, ?)",
                  ('income' if amount >= 0 else 'expense', amount, subject, file_path, folder_path, datetime.now()))
        conn.commit()
        
        # Copy file to folder
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            shutil.copy(file_path, folder_path)
        
        # Update file_path in the database
        c.execute("UPDATE transactions SET file_path=? WHERE id=?", (folder_path, c.lastrowid))
        conn.commit()
        
        # Create text file
        with open(os.path.join(folder_path, 'details.txt'), 'w') as file:
            file.write(f"Amount: {amount}\n")
            file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"File Path: {file_path}\n")
            file.write(f"Folder Path: {folder_path}\n")
        clear_entries()
        update_labels()
    except ValueError:
        clear_entries()
        message_label.config(text="Please enter a valid amount.", fg="red")
    update_listbox()

def delete_folder_from_database(db_file, transaction_id):
    try:
        # Connect to the database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Retrieve folder path from the database using the transaction ID
        cursor.execute("SELECT folder_path FROM transactions WHERE id=?", (transaction_id,))
        row = cursor.fetchone()
        
        if row:
            folder_path = row[0]

            # Delete the folder and its contents
            if os.path.exists(folder_path):
                print(f"Deleting folder: {folder_path}")
                try:
                    shutil.rmtree(folder_path)
                    print(f"Folder deleted: {folder_path}")
                except Exception as e:
                    print(f"Error deleting folder: {e}")
            else:
                print(f"Folder doesn't exist: {folder_path}")
        else:
            print(f"No folder path found for transaction ID: {transaction_id}")

        # Commit changes and close the connection
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error accessing database: {e}")


def delete_transaction():
    selected_id = transactions_listbox.curselection()
    if selected_id:
        id = transactions_listbox.get(selected_id[0]).split(':')[0]
        # Call delete_folder_from_database with the transaction ID
        delete_folder_from_database("finances.db", id)
        # Delete the transaction from the database
        c.execute("DELETE FROM transactions WHERE id=?", (id,))
        conn.commit()
        clear_entries()
        update_labels()
        update_listbox()


def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def print_report():
    with open('report.txt', 'w') as file:
        file.write(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write("Transaction History:\n\n")
        c.execute("SELECT * FROM transactions")
        for row in c.fetchall():
            file.write(f"ID: {row[0]}, Type: {row[1]}, Amount: {row[2]}, Subject: {row[3]}, File Path: {row[4]}, Date: {row[5]}\n")
    os.startfile('report.txt')

def open_files_folder():
    os.startfile('databases')

def clear_entries():
    amount_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    file_entry.delete(0, tk.END)

def update_labels():
    # Fetch data from the database and update labels
    c.execute("SELECT SUM(amount) FROM transactions")
    total_balance = c.fetchone()[0] or 0
    c.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_incomes = c.fetchone()[0] or 0
    c.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expenses = c.fetchone()[0] or 0
    
    total_balance_label.config(text=f"Total Balance: {total_balance}")
    total_incomes_label.config(text=f"Total Incomes: {total_incomes}")
    total_expenses_label.config(text=f"Total Expenses: {total_expenses}")

# UI Elements
def update_datetime():
    date_label.config(text=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    root.after(1000, update_datetime)

transactions_listbox = tk.Listbox(root, font=(font1,size1), fg=fg1, bg=bg2, width=28, height=26)
transactions_listbox.pack(side = tk.LEFT, padx=20, pady=10)
transactions_listbox.delete(0, tk.END)
update_listbox()

date_label = tk.Label(root, text=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), font=(font1, 11), fg="lightyellow", bg=bg1)
date_label.pack(pady=10)

update_datetime()

total_balance_label = tk.Label(root, text="Total Balance: TBD", font=(font1, 18), fg= "lightblue", bg=bg1)
total_balance_label.pack()

total_incomes_label = tk.Label(root, text="Total Incomes: TBD", font=(font1,size3), fg= "lightgreen", bg=bg1)
total_incomes_label.pack()

total_expenses_label = tk.Label(root, text="Total Expenses: TBD", font=(font1,size3), fg= "pink", bg=bg1)
total_expenses_label.pack()



amount_label = tk.Label(root, text="Enter new expense/income:", font=(font1,size1), fg=fg1, bg=bg1)
amount_label.pack()
amount_entry = tk.Entry(root, font=(font1,size1), fg=fg2, bg=bg1, width = 35)
amount_entry.pack(padx=10)

subject_label = tk.Label(root, text="Subject:", font=(font1,size1), fg=fg1, bg=bg1)
subject_label.pack()
subject_entry = tk.Entry(root, font=(font1,size1), fg=fg2, bg=bg1, width = 35)
subject_entry.pack(padx=10)

file_label = tk.Label(root, text="File:", font=(font1,size1), fg=fg1, bg=bg1)
file_label.pack()
file_entry = tk.Entry(root, font=(font1,size1), fg=fg2, bg=bg1, width = 35)
file_entry.pack(padx=10)

save_button = tk.Button(root, text="Save", font=(font1,size1), fg=fg1, bg=bg2, width=35, command=save_transaction)
save_button.pack(padx= 10, pady = 10)

delete_button = tk.Button(root, text="Delete", font=(font1,size1), fg=fg1, bg=bg2, width=35, command=delete_transaction)
delete_button.pack(padx= 10, pady = 10)

upload_button = tk.Button(root, text="Upload file", font=(font1,size1), fg=fg1, bg=bg2, width=35, command=upload_file)
upload_button.pack(padx= 10, pady = 10)

print_button = tk.Button(root, text="Print report", font=(font1,size1), fg=fg1, bg=bg2, width=35, command=print_report)
print_button.pack(padx= 10, pady = 10)

open_folder_button = tk.Button(root, text="Open files folder", font=(font1,size1), fg=fg1, bg=bg2, width=35, command=open_files_folder)
open_folder_button.pack(padx= 10, pady = 10)





message_label = tk.Label(root, text="",bg = bg1, fg=bg2)
message_label.pack()

# Initial label update
update_labels()

root.mainloop()
