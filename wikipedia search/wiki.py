from tkinter import *
import wikipedia as wiki

root = Tk()
root.title("Wikipedia Search")
root.geometry("900x800")
root.minsize(900, 700)
root.maxsize(900, 700)
root.configure(bg='#0D47A1')

# Clear
def clear():
    my_entry.delete(0, END)
    my_text.delete(1.0, END)

# Search
def search():
    try:
        result = wiki.page(my_entry.get())
        my_text.delete(1.0, END)
        my_text.insert(1.0, result.content)
    except wiki.exceptions.DisambiguationError as e:
        my_text.delete(1.0, END)
        my_text.insert(1.0, f"Disambiguation Error: {e.options}")
    except wiki.exceptions.PageError:
        my_text.delete(1.0, END)
        my_text.insert(1.0, "Page not found.")
    except Exception as e:
        my_text.delete(1.0, END)
        my_text.insert(1.0, f"An error occurred: {e}")

# Header
header_frame = Frame(root, bg='#0D47A1')
header_frame.pack(side=TOP, fill=X)

header_label = Label(header_frame, text='Wikipedia Search', font=('Helvetica', 20, 'bold'), fg='#FFFFFF', bg='#0D47A1')
header_label.pack(pady=10)

# Main
main_frame = Frame(root, bg='#0D47A1')
main_frame.pack(pady=5)

# Search Entry
my_entry = Entry(main_frame, font=("Helvetica", 14), width=80, bg="#FFFFFF", fg="#000000")
my_entry.pack(pady=5, padx=20)

# Bind the Enter key to the search function
my_entry.bind("<Return>", lambda event: search())

# Results
results_frame = Frame(root, bg='#E6E6E6')
results_frame.pack(pady=20)

# Text Box
my_text = Text(results_frame, wrap='word', height=26, width=100, font=("Helvetica", 12), bg='#FFFFFF', fg='#000000')
my_text.pack(fill=BOTH, expand=True)

# Footer
footer_frame = Frame(root, bg='#0D47A1')
footer_frame.pack(fill=X)

# Buttons
fake1_label = Label(footer_frame, text='                                  ', font=('Helvetica', 20, 'bold'), fg='#FFFFFF', bg='#0D47A1')
fake1_label.grid(row=0, column=0, padx=20)

search_button = Button(footer_frame, text="Search", font=("Helvetica", 14, 'bold'), fg='#FFFFFF', bg='#0D47A1', command=search)
search_button.grid(row=0, column=1, padx=20)

clear_button = Button(footer_frame, text="Clear", font=("Helvetica", 14, 'bold'), fg='#FFFFFF', bg='#0D47A1', command=clear)
clear_button.grid(row=0, column=2, padx=20)

fake2_label = Label(footer_frame, text='                      ', font=('Helvetica', 20, 'bold'), fg='#FFFFFF', bg='#0D47A1')
fake2_label.grid(row=0, column=3, padx=20)

search_img = PhotoImage(file="wikipedia.png")
fake_label = Label(footer_frame, image=search_img, bg="#0D47A1", borderwidth=0)
fake_label.grid(row=0, column=4, padx=20)

root.mainloop()
