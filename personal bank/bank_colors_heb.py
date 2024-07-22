import tkinter as tk
from tkinter import messagebox
import sqlite3
import atexit
from datetime import datetime
new_row = '''\n_______________________________________________________________________________\n'''
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
    print(f"Inserting transaction: Date/Time: {date_time}, Action: {action}, Amount: {amount}, Comment: {comment}")
    c.execute("INSERT INTO transactions (date_time, action, amount, comment) VALUES (?, ?, ?, ?)",
              (date_time, action, amount, comment))
    conn.commit()


def update_balances():
    global bank_conn, cash_conn
    
    # Calculate bank balance
    c_bank = bank_conn.cursor()
    c_bank.execute("SELECT SUM(amount) FROM transactions WHERE action='הפקדה'")
    bank_deposits = c_bank.fetchone()[0]
    bank_deposits = bank_deposits if bank_deposits else 0

    c_bank.execute("SELECT SUM(amount) FROM transactions WHERE action='משיכה'")
    bank_withdrawals = c_bank.fetchone()[0]
    bank_withdrawals = bank_withdrawals if bank_withdrawals else 0

    bank_balance = bank_deposits - bank_withdrawals

    # Calculate cash balance
    c_cash = cash_conn.cursor()
    c_cash.execute("SELECT SUM(amount) FROM transactions WHERE action='הפקדה'")
    cash_deposits = c_cash.fetchone()[0]
    cash_deposits = cash_deposits if cash_deposits else 0

    c_cash.execute("SELECT SUM(amount) FROM transactions WHERE action='משיכה'")
    cash_withdrawals = c_cash.fetchone()[0]
    cash_withdrawals = cash_withdrawals if cash_withdrawals else 0

    cash_balance = cash_deposits - cash_withdrawals

    return bank_balance, cash_balance





# Function to calculate total cash and bank balances
def calculate_total_balances():
    conn = bank_conn
    c = conn.cursor()
    c.execute("SELECT SUM(CASE WHEN action='הפקדה' THEN amount ELSE -amount END) FROM transactions")
    bank_total = c.fetchone()[0]
    bank_total = bank_total if bank_total else 0

    conn = cash_conn
    c = conn.cursor()
    c.execute("SELECT SUM(CASE WHEN action='הפקדה' THEN amount ELSE -amount END) FROM transactions")
    cash_total = c.fetchone()[0]
    cash_total = cash_total if cash_total else 0

    return bank_total, cash_total


def refresh_balances():
    global bank_balance_label, cash_balance_label
    bank_balance, cash_balance = update_balances()
    print("Bank balance:", bank_balance)
    print("Cash balance:", cash_balance)
    bank_balance_label.config(text=f"יתרת הבנק: {bank_balance:.2f} ש\"ח", font=("Arial", 12, "bold"), justify="right", fg="#008000" if bank_balance >= 0 else "#FF0000")
    cash_balance_label.config(text=f"יתרת המזומנים: {cash_balance:.2f} ש\"ח", font=("Arial", 12, "bold"), justify="right", fg="#008000" if cash_balance >= 0 else "#FF0000")


# Function to handle deposit or withdrawal
def handle_transaction(action, amount, comment, is_cash):
    if action == "משיכה":
        amount = -amount  # Ensure amount is negative for withdrawals
    if is_cash:
        insert_transaction(cash_conn, action, amount, comment)
    else:
        insert_transaction(bank_conn, action, amount, comment)
    refresh_balances()
    messagebox.showinfo("Success", f"ה{action} של ש''ח{amount:.2f} {comment} הושלמה בהצלחה.")


# Function to handle deposit button click
def deposit():
    amount = float(deposit_entry.get())
    comment = deposit_comment_entry.get()
    is_cash = deposit_to_bank.get() == 0
    handle_transaction("הפקדה", amount, comment, is_cash)

# Function to handle withdrawal button click
def withdraw():
    amount = float(withdraw_entry.get())
    comment = withdraw_comment_entry.get()
    is_cash = withdraw_from_bank.get() == 0
    # Ensure amount is negative for withdrawal
    handle_transaction("משיכה", -amount, comment, is_cash)

# Function to handle delete button click
def delete():
    id = int(delete_entry.get())
    conn = cash_conn if delete_from_bank.get() == 0 else bank_conn
    c = conn.cursor()
    c.execute("DELETE FROM transactions WHERE id=?", (id,))
    conn.commit()
    refresh_balances()
    messagebox.showinfo("Success", f"העסקה עם מספר זיהוי {id} נמחקה בהצלחה.")

def show_history():
    conn = bank_conn
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("היסטוריית העסקאות")

    cash_text2 = tk.Label(history_window, text="\n-בנק-\n", font=("Arial", 16))
    cash_text2.pack()
    
    history_text = tk.Text(history_window, font=("Arial", 14))
    history_text.pack(expand=True, fill="both")

    for row in rows:
        amount_color = "green" if row[2] == 'הפקדה' else "red"  # Green for Deposit, Red for Withdrawal
        history_text.insert(tk.END, f'    מספר זיהוי עסקה: {row[0]}, תאריך: {row[1]}, פעולה: {row[2]}, סכום: {row[3]:.2f} ש"ח, הערה: {row[4]}    {new_row}', amount_color)

    # Set text direction to right-to-left
    history_text.tag_configure("left", justify="left")
    history_text.tag_configure('green', foreground='green')
    history_text.tag_configure('red', foreground='red')
    history_text.insert("1.0", " ", "right")

def show_cash_transactions():
    conn = cash_conn
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()

    cash_transactions_window = tk.Toplevel(root)
    cash_transactions_window.title("העסקאות במזומנים")

    cash_transactions_text2 = tk.Label(cash_transactions_window, text="\n-מזומנים-\n", font=("Arial", 16))
    cash_transactions_text2.pack()
    
    cash_transactions_text = tk.Text(cash_transactions_window, font=("Arial", 14))
    cash_transactions_text.pack(expand=True, fill="both")

    for row in rows:
        amount_color = "green" if row[2] == 'הפקדה' else "red"  # Green for Deposit, Red for Withdrawal
        cash_transactions_text.insert(tk.END, f'    מספר זיהוי עסקה: {row[0]}, תאריך: {row[1]}, פעולה: {row[2]}, סכום: {row[3]:.2f} ש"ח, הערה: {row[4]}    {new_row}', amount_color)

    # Set text direction to right-to-left
    cash_transactions_text.tag_configure("left", justify="left")
    cash_transactions_text.tag_configure('green', foreground='green')
    cash_transactions_text.tag_configure('red', foreground='red')
    cash_transactions_text.insert("1.0", " ", "right")



# Function to close database connections
def close_connections():
    bank_conn.close()
    cash_conn.close()

# Create the GUI window
root = tk.Tk()
root.title("מערכת ניהול בנק")

# Open database connections
bank_conn = sqlite3.connect('bank.db')
cash_conn = sqlite3.connect('cash.db')

# Create database tables
create_table(bank_conn)
create_table(cash_conn)

# Register function to close connections on program exit
atexit.register(close_connections)

# Deposit Section
deposit_frame = tk.LabelFrame(root, text="הפקדה", font=("Arial", 14))
deposit_frame.grid(row=0, column=0, padx=10, pady=10)
deposit_label = tk.Label(deposit_frame, text=" סכום", font=("Arial", 14))
deposit_label.grid(row=0, column=1, padx=5, pady=5)
deposit_entry = tk.Entry(deposit_frame)
deposit_entry.grid(row=0, column=0, padx=5, pady=5)
deposit_comment_label = tk.Label(deposit_frame, text=" הערה", font=("Arial", 14))
deposit_comment_label.grid(row=1, column=1, padx=5, pady=5)
deposit_comment_entry = tk.Entry(deposit_frame)
deposit_comment_entry.grid(row=1, column=0, padx=5, pady=5)
deposit_to_bank = tk.IntVar()
deposit_check = tk.Checkbutton(deposit_frame, text="הפקד לבנק", variable=deposit_to_bank)
deposit_check.grid(row=2, columnspan=2, padx=5, pady=5)
deposit_button = tk.Button(deposit_frame, text="הפקד", command=deposit)
deposit_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Withdraw Section
withdraw_frame = tk.LabelFrame(root, text="משיכה", font=("Arial", 14))
withdraw_frame.grid(row=0, column=1, padx=10, pady=10)
withdraw_label = tk.Label(withdraw_frame, text=" סכום", font=("Arial", 14))
withdraw_label.grid(row=0, column=1, padx=5, pady=5)
withdraw_entry = tk.Entry(withdraw_frame)
withdraw_entry.grid(row=0, column=0, padx=5, pady=5)
withdraw_comment_label = tk.Label(withdraw_frame, text=" הערה", font=("Arial", 14))
withdraw_comment_label.grid(row=1, column=1, padx=5, pady=5)
withdraw_comment_entry = tk.Entry(withdraw_frame)
withdraw_comment_entry.grid(row=1, column=0, padx=5, pady=5)
withdraw_from_bank = tk.IntVar()
withdraw_check = tk.Checkbutton(withdraw_frame, text="משיכה מהבנק", variable=withdraw_from_bank)
withdraw_check.grid(row=2, columnspan=2, padx=5, pady=5)
withdraw_button = tk.Button(withdraw_frame, text="משיכה", command=withdraw)
withdraw_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Delete Section
delete_frame = tk.LabelFrame(root, text="מחיקת עסקה", font=("Arial", 14))
delete_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
delete_label = tk.Label(delete_frame, text="מספר זיהוי עסקה:")
delete_label.grid(row=0, column=1, padx=5, pady=5)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=0, padx=5, pady=5)
delete_from_bank = tk.IntVar()
delete_check = tk.Checkbutton(delete_frame, text="מחיקה מהבנק", variable=delete_from_bank)
delete_check.grid(row=1, columnspan=2, padx=5, pady=5)
delete_button = tk.Button(delete_frame, text="מחיקה", command=delete)
delete_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Balance Section
balance_frame = tk.LabelFrame(root, text="מאזן", font=("Arial", 14))
balance_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
bank_balance_label = tk.Label(balance_frame, text='יתרת הבנק:  0.00 ש"ח', font=("Arial", 12, "bold"), justify="right")
bank_balance_label.grid(row=0, column=0, padx=5, pady=5)
cash_balance_label = tk.Label(balance_frame, text='יתרת המזומנים:  0.00 ש"ח', font=("Arial", 12, "bold"), justify="right")
cash_balance_label.grid(row=1, column=0, padx=5, pady=5)

# History Button
history_button = tk.Button(root, text="הצג היסטוריה בבנק", command=show_history)
history_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Cash Transactions Button
cash_transactions_button = tk.Button(root, text="הצג הסטוריה במזומנים", command=show_cash_transactions)
cash_transactions_button.grid(row=4, column=0, columnspan=2, padx=250, pady=30)

# Call refresh_balances() after GUI initialization to update balance labels
refresh_balances()

# Start the GUI
root.mainloop()



