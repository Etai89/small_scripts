from tkinter import *
root = Tk()
root.title('databashhhhhh')
root.geometry("800x521")# + "169+32")


##   variables:
txt = Text(root)


##  defenitions

#  change window size by entering width and height values.
def resize():
    w = width_entry.get()
    h = height_entry.get()

    root.geometry(f"{w}x{h}")

width_label = Label(root, text="width:")
width_label.pack(pady=2)
width_entry = Entry(root)
width_entry.pack(pady=2)

height_label = Label(root, text="height:")
height_label.pack(pady=2)
height_entry = Entry(root)
height_entry.pack(pady=2)

#  print the (width, heigh, x, y) information 
## print the info in 1 line
def info():
    geometry_info = "height: " + str(root.winfo_height()) + ", width: " + str(root.winfo_width()) + ", X: " + str(root.winfo_x()) + ", Y: " + str(root.winfo_y())
    dimention_label = Label(root, text=geometry_info)
    dimention_label.pack()


## print the information  
def info2():
    dimention_label = Label(root, text=root.winfo_geometry())
    dimention_label.pack(pady=2)

    height_label = Label(root, text="height: " + str(root.winfo_height()))
    height_label.pack(side="top",pady=2)
    width_label = Label(root, text="width: " + str(root.winfo_width()))
    width_label.pack(side="top",pady=2)

    x_label = Label(root, text="X: " + str(root.winfo_x()))
    x_label.pack(side="top", pady=2)
    y_label = Label(root, text="Y: " + str(root.winfo_y()))
    y_label.pack(side="top",pady=2)
    pop = (height_label, width_label, x_label, y_label)

    pop.pack(pady=20)   
    
def copy_all():
    root.clipboard_clear()
    root.clipboard_append(txt.get(1.0, END))

#  buttons
resize_button = Button(root, text="resize", command=resize)
check_rez = Button(root, text="check rezolution", command=info2)
copy_all_button = Button(root, text="copy", command=copy_all)

#  buttons packing
resize_button.pack(pady=2)
check_rez.pack(pady=2)
copy_all_button.pack(pady=2)

root.mainloop()        
