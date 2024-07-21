from tkinter import *
from tkinter import messagebox, filedialog
from random import choice, randint, shuffle
import random
import os
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
import pyperclip
from tkinter import ttk
from tkinter import simpledialog


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
import tkinter as tk
from random import choice, randint, shuffle

# Define the generate_password function
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    len1 = len(password)
    OPEN_LABEL_TEXT = f'Passwrord Length: {len1}'
    open_fil_label = Label(text=OPEN_LABEL_TEXT, bg=BG, fg=FG, font=(FONT, FSIZE))
    open_fil_label.grid(row=5, column=1)
    
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email}"
                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Open the existing data file or create a new one if it doesn't exist
            try:
                with open("pass1.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = []

            # Append the new password data to the list
            numbers = len(data) + 1
            new_data = {
                "id": numbers,
                "website": website,
                "email": email,
                "password": password
            }
            data.append(new_data)

            # Save the updated data to the file
            with open("pass1.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)



def open_file():
    with open("pass1.json") as data_file:
        data = json.load(data_file)
        if data:
            text_widget = Text(window, width=65, height=20, font=("Tahoma", 13),bg='black', fg="green")
            text_widget.grid(row=6, column=0, columnspan=3, padx=5, pady=2)
            
            for item in data:
                text_widget.insert(END, f"ID: {item['id']}\n")
                text_widget.insert(END, f"Website:        {item['website']}\n")
                text_widget.insert(END, f"Email:             {item['email']}\n")
                text_widget.insert(END, f"Password:     {item['password']}\n\n")

            text_widget.config(state=DISABLED)
        else:
            messagebox.showinfo(title="Error", message="No data to display.")

try:
    with open("pass1.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# Function to save data to file
def save_data(name, age):
    data.append({"name": name, "age": age})
    with open("pass1.json", "w") as f:
        json.dump(data, f, indent=2)

# Function to delete data from file
def delete_data():
    # Open the existing data file or create a new one if it doesn't exist
    try:
        with open("pass1.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = []

    # Prompt user for id to delete
    id_name = simpledialog.askstring(title="Delete Data",prompt="Please enter ID to delete:")
    if id_name:
        # Remove all entries for the website and save changes to file
        data = [item for item in data if item["id"] != int(id_name)]
        with open("pass1.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
            messagebox.showinfo(title="Success", message="Selected data has been deleted.")
        
        # Update the ids of the remaining items in the list
        for i, item in enumerate(data):
            item["id"] = i + 1
        with open("pass1.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    # Counter for saved data
    counter = len(data) + 1



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10, bg='black')
window.geometry("+293+78")

BG = 'black'
FG = 'green'
# Canvas
##canvas = Canvas(height=350, width=600)
####logo_img = PhotoImage(file="1/snoop.gif")
####canvas.create_image(320, 170, image=logo_img)
##canvas.grid(row=0, column=0, columnspan=3)


FONT = 'Tahoma'
FSIZE = 12
# Labels
website_label = Label(text="Website", bg=BG, fg=FG, font=(FONT, FSIZE))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username", bg=BG, fg=FG, font=(FONT, FSIZE))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=BG, fg=FG, font=(FONT, FSIZE))
password_label.grid(row=3, column=0, padx=78)


# Entries
website_entry = Entry(width=45, bg=BG, fg=FG, font=(FONT, FSIZE))
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
# put cursor on the entry when program prompt
website_entry.focus()
email_entry = Entry(width=45, bg=BG, fg=FG, font=(FONT, FSIZE))
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

# Open the JSON file and load the data into a dictionary

with open('authentication.json') as f:
    auth_data = json.load(f)

# Access the individual authentication details using the dictionary keys
email_json = auth_data['email']
email_entry.insert(0, email_json)
password_entry = Entry(width=26, bg=BG, fg=FG, font=(FONT, FSIZE))
password_entry.grid(sticky="ew", row=3, column=1, padx=0, pady=1)

#buttons

generate_password_button = Button(text="Generate Password", font=(FONT, FSIZE), bg=BG, fg=FG, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", bg=BG, fg=FG, width=15, font=(FONT, FSIZE), command=save)
add_button.grid(row=4, column=2, columnspan=2,  pady=5)

open_button = Button(text="Show Passwords", font=(FONT, FSIZE), bg=BG, fg=FG, width=15, command=open_file)
open_button.grid(row=4, column=0,  pady=5)

delete_button = Button(text="Delete", font=(FONT, FSIZE), width=15, bg=BG, fg=FG, command=delete_data)
delete_button.grid(row=4, column=1,  pady=5)

window.mainloop()



'''
messagebox.showinfo(title="show info", message="Password Saved !")
messagebox.askyesno(title="yes no ", message="yes no !")
messagebox.askquestion(title="question ", message="you like monkeys?")
messagebox.yesno(title="ok cancel ", message="ok or cancel !")
'''
