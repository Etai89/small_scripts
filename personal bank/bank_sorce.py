import tkinter as tk
from tkinter import messagebox
import sqlite3
import atexit
from datetime import datetime

# Declare global variables for balance labels and database connections
bank_balance_label = None
cash_balance_label = None
bank_conn = None
cash_conn = None

# Function to create the database table if not exists
def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, date_time TEXT, action TEXT, amount REAL, comment TEXT)''')
    conn.commit()

# Function to insert a transaction into the database
def insert_transaction(conn, action, amount, comment):
    c = conn.cursor()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO transactions (date_time, action, amount, comment) VALUES (?, ?, ?, ?)",
              (date_time, action, amount, comment))
    conn.commit()

# Function to update the balances
def update_balances():
    global bank_conn, cash_conn
    c_bank = bank_conn.cursor()
    c_cash = cash_conn.cursor()
    c_bank.execute("SELECT SUM(CASE WHEN action='Deposit' THEN amount WHEN action='Withdrawal' THEN -amount ELSE 0 END) FROM transactions")
    bank_balance = c_bank.fetchone()[0]
    bank_balance = bank_balance if bank_balance else 0
    c_cash.execute("SELECT SUM(CASE WHEN action='Deposit' THEN amount WHEN action='Withdrawal' THEN -amount ELSE 0 END) FROM transactions")
    cash_balance = c_cash.fetchone()[0]
    cash_balance = cash_balance if cash_balance else 0
    return bank_balance, cash_balance

# Function to refresh balances and display them
def refresh_balances():
    global bank_balance_label, cash_balance_label
    bank_balance, cash_balance = update_balances()
    bank_balance_label.config(text=f"Bank Balance: ${bank_balance:.2f}", font=("Arial", 12, "bold"), justify="right")
    cash_balance_label.config(text=f"Cash Balance: ${cash_balance:.2f}", font=("Arial", 12, "bold"), justify="right")

# Function to handle deposit or withdrawal
def handle_transaction(action, amount, comment, is_cash):
    if action == "Withdrawal":
        amount = -amount
    if is_cash:
        insert_transaction(cash_conn, action, amount, comment)
    else:
        insert_transaction(bank_conn, action, amount, comment)
    refresh_balances()
    messagebox.showinfo("Success", f"{action} of ${amount:.2f} {comment} completed successfully.")

# Function to handle deposit button click
def deposit():
    amount = float(deposit_entry.get())
    comment = deposit_comment_entry.get()
    is_cash = deposit_to_bank.get() == 0
    handle_transaction("Deposit", amount, comment, is_cash)

# Function to handle withdrawal button click
def withdraw():
    amount = float(withdraw_entry.get())
    comment = withdraw_comment_entry.get()
    is_cash = withdraw_from_bank.get() == 0
    # Ensure amount is negative for withdrawal
    handle_transaction("Withdrawal", -amount, comment, is_cash)

# Function to handle delete button click
def delete():
    id = int(delete_entry.get())
    conn = cash_conn if delete_from_bank.get() == 0 else bank_conn
    c = conn.cursor()
    c.execute("DELETE FROM transactions WHERE id=?", (id,))
    conn.commit()
    refresh_balances()
    messagebox.showinfo("Success", f"Transaction with ID {id} deleted successfully.")

# Function to display transaction history
def show_history():
    conn = bank_conn
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("Transaction History")

    history_text = tk.Text(history_window, font=("Arial", 12))
    history_text.pack(expand=True, fill="both")

    for row in rows:
        history_text.insert(tk.END, f"Transaction ID: {row[0]}, Date: {row[1]}, Action: {row[2]}, Amount: {row[3]:.2f}, Comment: {row[4]}\n")

    # Set text direction to right-to-left
    history_text.tag_configure("right", justify="right")
    history_text.insert("1.0", " ", "right")

# Function to display cash transactions
def show_cash_transactions():
    conn = cash_conn
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()

    cash_transactions_window = tk.Toplevel(root)
    cash_transactions_window.title("Cash Transactions")

    cash_transactions_text = tk.Text(cash_transactions_window, font=("Arial", 12))
    cash_transactions_text.pack(expand=True, fill="both")

    for row in rows:
        cash_transactions_text.insert(tk.END, f"Transaction ID: {row[0]}, Date: {row[1]}, Action: {row[2]}, Amount: {row[3]:.2f}, Comment: {row[4]}\n")

    # Set text direction to right-to-left
    cash_transactions_text.tag_configure("right", justify="right")
    cash_transactions_text.insert("1.0", " ", "right")

# Function to close database connections
def close_connections():
    bank_conn.close()
    cash_conn.close()

# Create the GUI window
root = tk.Tk()
root.title("Bank Management System")

# Open database connections
bank_conn = sqlite3.connect('bank.db')
cash_conn = sqlite3.connect('cash.db')

# Create database tables
create_table(bank_conn)
create_table(cash_conn)

# Register function to close connections on program exit
atexit.register(close_connections)

# Deposit Section
deposit_frame = tk.LabelFrame(root, text="Deposit")
deposit_frame.grid(row=0, column=0, padx=10, pady=10)
deposit_label = tk.Label(deposit_frame, text="Amount:")
deposit_label.grid(row=0, column=0, padx=5, pady=5)
deposit_entry = tk.Entry(deposit_frame)
deposit_entry.grid(row=0, column=1, padx=5, pady=5)
deposit_comment_label = tk.Label(deposit_frame, text="Comment:")
deposit_comment_label.grid(row=1, column=0, padx=5, pady=5)
deposit_comment_entry = tk.Entry(deposit_frame)
deposit_comment_entry.grid(row=1, column=1, padx=5, pady=5)
deposit_to_bank = tk.IntVar()
deposit_check = tk.Checkbutton(deposit_frame, text="Deposit to Bank", variable=deposit_to_bank)
deposit_check.grid(row=2, columnspan=2, padx=5, pady=5)
deposit_button = tk.Button(deposit_frame, text="Deposit", command=deposit)
deposit_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Withdraw Section
withdraw_frame = tk.LabelFrame(root, text="Withdraw")
withdraw_frame.grid(row=0, column=1, padx=10, pady=10)
withdraw_label = tk.Label(withdraw_frame, text="Amount:")
withdraw_label.grid(row=0, column=0, padx=5, pady=5)
withdraw_entry = tk.Entry(withdraw_frame)
withdraw_entry.grid(row=0, column=1, padx=5, pady=5)
withdraw_comment_label = tk.Label(withdraw_frame, text="Comment:")
withdraw_comment_label.grid(row=1, column=0, padx=5, pady=5)
withdraw_comment_entry = tk.Entry(withdraw_frame)
withdraw_comment_entry.grid(row=1, column=1, padx=5, pady=5)
withdraw_from_bank = tk.IntVar()
withdraw_check = tk.Checkbutton(withdraw_frame, text="Withdraw from Bank", variable=withdraw_from_bank)
withdraw_check.grid(row=2, columnspan=2, padx=5, pady=5)
withdraw_button = tk.Button(withdraw_frame, text="Withdraw", command=withdraw)
withdraw_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Delete Section
delete_frame = tk.LabelFrame(root, text="Delete Transaction")
delete_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
delete_label = tk.Label(delete_frame, text="Transaction ID:")
delete_label.grid(row=0, column=0, padx=5, pady=5)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=1, padx=5, pady=5)
delete_from_bank = tk.IntVar()
delete_check = tk.Checkbutton(delete_frame, text="Delete from Bank", variable=delete_from_bank)
delete_check.grid(row=1, columnspan=2, padx=5, pady=5)
delete_button = tk.Button(delete_frame, text="Delete", command=delete)
delete_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Balance Section
balance_frame = tk.LabelFrame(root, text="Balances")
balance_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
bank_balance_label = tk.Label(balance_frame, text="Bank Balance: $0.00", font=("Arial", 12, "bold"), justify="right")
bank_balance_label.grid(row=0, column=0, padx=5, pady=5)
cash_balance_label = tk.Label(balance_frame, text="Cash Balance: $0.00", font=("Arial", 12, "bold"), justify="right")
cash_balance_label.grid(row=1, column=0, padx=5, pady=5)

# History Button
history_button = tk.Button(root, text="Show Transaction History", command=show_history)
history_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Cash Transactions Button
cash_transactions_button = tk.Button(root, text="Show Cash Transactions", command=show_cash_transactions)
cash_transactions_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Refresh Balances only after GUI initialization
refresh_balances()

# Start the GUI
root.mainloop()
