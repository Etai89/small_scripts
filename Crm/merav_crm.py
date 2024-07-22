import tkinter as tk
from tkinter import Text
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image


E_W = '30'
c1 = 'pink'
c2 = 'purple'
c3 = 'lightblue'
c4 = 'purple'
c5= 'lightyellow'
f1 = 'Tahoma'
s1 = '10'
y1 = '4'
x1 = '4'

def submit():
    if entry_name.get().strip() == '' or entry_phone.get().strip() == '' or entry_email.get().strip() == '' or entry_message.get().strip() == '':
        # Show an error message and return
        messagebox.showerror("שגיאה", "צריך למלא את כל השדות\nשם, Email, טלפון, טיפול")
        return

    conn = sqlite3.connect('merav_database.db')
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS students (
                    name text,
                    email text,
                    phone text,
                    message text
                )""")
    
    c.execute("INSERT INTO students VALUES (?,?,?,?)",
              (entry_name.get(), entry_email.get(), entry_phone.get(), entry_message.get()))
    conn.commit()
    conn.close()
    
    fetch_data()
    messagebox.showinfo( 'שמירת לקוחה חדשה', f' הלקוחה {entry_name.get()} נוספה בהצלחה !')
    clear_entries()
    
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_message.delete(0, tk.END)
    text_box.delete('1.0', tk.END)

def fetch_data():
    conn = sqlite3.connect('merav_database.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM students")
    records = c.fetchall()
    print_records = ""
    for record in records:
        print_records += record[3] + " | " + record[2] + " | " + record[1] + " | " + record[0] + " | " + str(record[4]) + "\n"
    text_box.delete('1.0', tk.END)  # clear existing text
    text_box.insert(tk.END, print_records)
    conn.commit()
    conn.close()


frame_text = ""


# Define entry_delete in the global scope
load_entry = None

def edit_record():
    conn = sqlite3.connect('merav_database.db')
    c = conn.cursor()

    # Create a new window
    edit_window = tk.Toplevel(root)
    edit_window.title("עריכת לקוחה קיימת")
    edit_window.config(bg=c1)
    

    def delete_record():
        # Delete the record from the database
        c.execute("DELETE FROM students WHERE oid = " + load_entry.get())
        conn.commit()

        # Update the remaining records' IDs
        c.execute("SELECT oid, * FROM students")
        records = c.fetchall()
        for i in range(len(records)):
            c.execute("UPDATE students SET oid = ? WHERE oid = ?", (i+1, records[i][0]))
        conn.commit()

            # Show a success message and update the GUI
        messagebox.showinfo("מחיקת ערך", f"הערך {load_entry.get()} נמחק בהצלחה!")
        load_entry.delete(0, tk.END)
        fetch_data()
        load_entry.delete(0, tk.END)
    
    def save_changes(record_id, entry_name, entry_phone, entry_email, entry_message):
        record_id = load_entry.get()
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        message = entry_message.get()

        # check if any of the fields are empty
        if name.strip() == '' or phone.strip() == '' or email.strip() == '' or message.strip() == '':
            messagebox.showerror("Error", "One or more entries are empty.")
            return

        # update record in database
        db.update_record(record_id, name, phone, email, message)

        # clear entry fields
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_message.delete(0, tk.END)


    def save_record():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        message = entry_message.get()

        
    

        # add record to database
        record_id = db.add_record(name, phone, email, message)

        # create label to show success message
        success_label = tk.Label(edit_window, text="הרשומה נשמרה בהצלחה")
        success_label.grid(row=6, column=0)

        # clear entry fields
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_message.delete(0, tk.END)

        # set the record_id in the save_button command
        save_button = tk.Button(edit_window, text="שמור", command=lambda: save_changes(record_id))
        save_button.grid(row=4, column=0)

    def load_record():
        conn = sqlite3.connect('merav_database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM students WHERE oid=?", (load_entry.get(),))
        record = c.fetchone()

        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_message.delete(0, tk.END)

        if record:
            entry_name.insert(tk.END, record[0])
            entry_email.insert(tk.END, record[1])
            entry_phone.insert(tk.END, record[2])
            entry_message.insert(tk.END, record[3])
        else:
            messagebox.showerror("שגיאה", f"הלקוחה עם המזהה '{load_entry.get()}' לא נמצאה")

        conn.close()


    # Labels and Entries
    load_label = tk.Label(edit_window, text="מספר לקוחה",bg=c1, fg=c4, font=(f1, s1))
    load_label.grid(row=0, column=1, pady='10')
    name_label = tk.Label(edit_window, text="שם",bg=c1, fg=c4, font=(f1, s1))
    name_label.grid(row=2, column=1)
    email_label = tk.Label(edit_window, text="Email",bg=c1, fg=c4, font=(f1, s1))
    email_label.grid(row=3, column=1)
    phone_label = tk.Label(edit_window, text="טלפון",bg=c1, fg=c4, font=(f1, s1))
    phone_label.grid(row=4, column=1)
    message_label = tk.Label(edit_window, text="טיפול",bg=c1, fg=c4, font=(f1, s1))
    message_label.grid(row=5, column=1)

    
    load_entry = tk.Entry(edit_window, bg=c3, fg=c4, font=(f1, s1))
    load_entry.grid(row=0, column=0, pady='10', padx='10')
    load_entry.focus_set()
    
    entry_name = tk.Entry(edit_window, bg=c3, fg=c4, font=(f1, s1))
    entry_name.grid(row=2, column=0)

    entry_email = tk.Entry(edit_window, bg=c3, fg=c4, font=(f1, s1))
    entry_email.grid(row=3, column=0)

    entry_phone = tk.Entry(edit_window, bg=c3, fg=c4, font=(f1, s1))
    entry_phone.grid(row=4, column=0)

    entry_message = tk.Entry(edit_window, bg=c3, fg=c4, font=(f1, s1))
    entry_message.grid(row=5, column=0)


    # Save and Cancel buttons
    save_button = tk.Button(edit_window, text="שמור", bg=c5, fg=c2, font=(f1, s1), command=lambda: save_changes(record_id))
    save_button.grid(row=6, column=0, pady=10)

    cancel_button = tk.Button(edit_window, text="בטל", bg=c5, fg=c2, font=(f1, s1), command=edit_window.destroy)
    cancel_button.grid(row=6, column=1, pady=10)

    delete_button = tk.Button(edit_window, text="מחק לקוחה", bg=c5, fg=c2, font=(f1, s1), command=delete_record)
    delete_button.grid(row=1, column=0, pady=10, padx=10)

    load_button = tk.Button(edit_window, text="טען לקוחה", bg=c5, fg=c2, font=(f1, s1), command=load_record)
    load_button.grid(row=1, column=1, pady=10, padx=10)
    
    edit_window.mainloop()

   


def on_entry_click(event):
    """Clears the entry widget when clicked."""
    entry_id.delete(0, tk.END)



root = tk.Tk()
root.config(bg=c2)
root.title("מירב - מערכת לנהיול כללי")
# Set the window icon to a solid red image
icon = tk.PhotoImage(width=1, height=1)
icon.put("purple", (0,0))
root.iconphoto(True, icon)

# Load the image file
##img = Image.open("merav_france.jpeg")
##img = img.resize((200, 180), resample=Image.LANCZOS) # Resize the image
##img = ImageTk.PhotoImage(img)
# Create a label to display the image
##img_label = tk.Label(root, image=img)

# Add the label to the window using the pack layout manager
##img_label.pack(side='top', padx=10, pady=10) # Set the anchor parameter to 'w' to align to the left


# Frame
frame1 = tk.Frame(root, bg=c1)
frame1.pack(side='top', pady='15', padx='15', anchor='w')


# Labels
space_label = tk.Label(frame1, text='', bg=c1)
space_label.grid(row=0, column=1)

name_label = tk.Label(frame1, text="שם",bg=c1, fg=c4, font=(f1, s1))
name_label.grid(row=1, column=1, pady=y1)

email_label = tk.Label(frame1, text="Email",bg=c1, fg=c4, font=(f1, s1))
email_label.grid(row=2, column=1, pady=y1)

phone_label = tk.Label(frame1, text="טלפון",bg=c1, fg=c4, font=(f1, s1))
phone_label.grid(row=3, column=1, pady=y1)

message_label = tk.Label(frame1, text="טיפול",bg=c1, fg=c4, font=(f1, s1))
message_label.grid(row=4, column=1, pady=y1)

##id_label = tk.Label(frame1, text="בחירת מספר לקוחה לעריכה\מחיקה")
##id_label.grid(row=5, column=1)

# Entries

entry_name = tk.Entry(frame1, width=E_W, bg=c3, fg=c4, font=(f1, s1))
entry_name.grid(row=1, column=0, columnspan=2, pady=y1, padx=x1)
entry_name.focus_set()
entry_email = tk.Entry(frame1, width=E_W, bg=c3, fg=c4, font=(f1, s1))
entry_email.grid(row=2, column=0, columnspan=2, pady=y1)

entry_phone = tk.Entry(frame1, width=E_W, bg=c3, fg=c4, font=(f1, s1))
entry_phone.grid(row=3, column=0, columnspan=2, pady=y1)

entry_message = tk.Entry(frame1, width=E_W, bg=c3, fg=c4, font=(f1, s1))
entry_message.grid(row=4, column=0, columnspan=2, pady=y1)


# confirm label

id_label = tk.Label(frame1, text=frame_text, bg=c1)
id_label.grid(row=5, column=0, columnspan=3)



# Buttons
submit_button = tk.Button(frame1, text="שמור לקוחה חדשה", bg=c5, fg=c2, font=(f1, s1), command=submit)
submit_button.grid(row=6, column=1, columnspan=1, pady=10, padx=10, ipadx=90)

fetch_button = tk.Button(frame1, text="תראה נתונים", bg=c5, fg=c2, font=(f1, s1), command=fetch_data)
fetch_button.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=85)

clear_button = tk.Button(frame1, text="נקה הכל", bg=c5, fg=c2, font=(f1, s1), command=clear_entries)
clear_button.grid(row=7, column=0, columnspan=1, pady=10, padx=10, ipadx=95)

edit_button = tk.Button(frame1, text="עריכת לקוחה קיימת", bg=c5, fg=c2, font=(f1, s1), command=edit_record)
edit_button.grid(row=7, column=1, columnspan=1, pady=10, padx=10, ipadx=85)


# Textbox
text_box = Text(frame1, width='50', heigh='10', bg=c3, fg=c2, font=(f1, 12))
text_box.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=95)


root.mainloop()

