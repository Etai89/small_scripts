import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import time
# for resizer uncomment
#from PIL import ImageTk, Image

root = Tk()
root.title("Universal Pictures Convertor")
root.geometry("1017x730")


# Define image
# for resizer uncomment
#bgpic = ImageTk.PhotoImage(file='buldog.gif')
##bgpic = PhotoImage(file='buldog.gif')

# Create a Canvas
my_canvas = Canvas(root, width=1017, height=730, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Set image in Canvas
##my_canvas.create_image(0,0, image=bgpic, anchor="nw")

# Add a Label
my_canvas.create_text(507, 30, text="Universal Pictures Convertor", font=("Thoma", 40), fill="orange")


def select_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, END)
    input_folder_entry.insert(0, input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, END)
    output_folder_entry.insert(0, output_folder)


'''
#supported_formats = ["BMP", "EPS", "GIF", "ICNS", "ICO", "IM", "JPEG", "JPEG 2000", "MSP", "PCX", "PNG", "PPM", "SGI", "SPIDER", "TGA", "TIFF", "WebP", "XBM"]
def from_listbox():
    selected_index = listbox.curselection()[0, END]
    lLabel["text"] = listbox.get(selected_index)
    

listbox = Listbox(root)
listbox.bind("<<ListboxSelect>>", lambda x: from_listbox())

formats = ["BMP", "EPS", "GIF", "ICNS", "ICO", "IM", "JPEG", "JPEG 2000", "MSP", "PCX", "PNG", "PPM", "SGI", "SPIDER", "TGA", "TIFF", "WebP", "XBM"]

for item in formats:
    listbox.insert("item", ["17"])

# add the listbox to the canvas using the pack geometry manager
my_canvas.create_window(10, 250, anchor="nw", window=listbox)

'''

formats = ["BMP", "EPS", "GIF", "ICNS", "ICO", "IM", "JPEG", "JPEG 2000", "MSP", "PCX", "PNG", "PPM", "SGI", "SPIDER", "TGA", "TIFF", "WebP", "XBM"]

# Calculate the position of the text
x = 950
y = 50
for format in formats:
    my_canvas.create_text(x, y, text=format)
    y += 20



import os

def list_image_files(folder_path, supported_formats):
    image_files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1]
            if file_extension.upper() in supported_formats:
                image_files.append(filename)
    return image_files


def convert_to_format(input_folder, output_folder, format, width, height):
    for filename in os.listdir(input_folder):
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Resize image
            if width and height:
                img = img.resize((int(width), int(height)))
            elif width:
                wpercent = (int(width) / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((int(width), hsize))
            elif height:
                hpercent = (int(height) / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercent)))
                img = img.resize((wsize, int(height)))
            
            # Save in user-specified format
            if not filename.endswith('.' + format):
                filename = os.path.splitext(filename)[0] + "." + format
            img.save(os.path.join(output_folder, filename), format.upper())

def convert():
    format = format_entry.get()
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    convert_to_format(input_folder, output_folder, format, width, height,)
    conv_message = my_canvas.create_text(507, 500, text="Convertions Completed !", font=("Thoma", 30), fill="orange")
    time.sleep(2)
    conv_message.destroy()

def exit_out():
    conv_message = my_canvas.create_text(507, 500, text="Exit !", font=("Thoma", 30), fill="orange")
    time.sleep(0.2)
    exit()


### Define entry_clear function
##def entry_clear1(e):
##     width_entry.delete(0, END)
##     if width_entry.get() == "":
##         return width_entry.get()  
##def entry_clear2(e):
##    height_entry.delete(0, END)
##def entry_clear3(e):
##    format_entry.delete(0, END)    


# Add some buttons
button1 = Button(root, text="Select Input folder", command = select_input_folder)
button2 = Button(root, text="Select Output folder", command=select_output_folder)
button3 = Button(root, text="Convert", width=15, height=2, command=convert)
button4 = Button(root, text="Exit", width=15, height=0, command=exit_out)

# Position the buttons in the canvas
button1_window = my_canvas.create_window(10, 60, anchor="nw", window=button1)
button2_window = my_canvas.create_window(10, 140, anchor="nw", window=button2)
button3_window = my_canvas.create_window(417, 170, anchor="nw", window=button3)
button4_window = my_canvas.create_window(417, 230, anchor="nw", window=button4)

# Define Entry Boxes
width_entry = Entry(root, font=("Helvetica", 24), width=6, fg= "#336d92", bd=0)
height_entry = Entry(root, font=("Helvetica", 24), width=6, fg= "#336d92", bd=0)
format_entry = Entry(root, font=("Helvetica", 24), width=6, fg= "#336d92", bd=0)
input_folder_entry = Entry(root, font=("Helvetica", 20), width=10, fg= "#336d92", bd=0)
output_folder_entry = Entry(root, font=("Helvetica", 20), width=10, fg= "#336d92", bd=0)


# Insert Place holders
width_entry.insert(0, "Width:")
height_entry.insert(0, "Height:")
format_entry.insert(0, "Format:")
input_folder_entry.insert(0, "input:")
output_folder_entry.insert(0, "output:")
# Add the Entry boxes to the Canvas
input_folder_entry_window = my_canvas.create_window(10, 100, anchor="nw", window=input_folder_entry)
output_folder_entry_window = my_canvas.create_window(10, 180, anchor="nw", window=output_folder_entry)
width_entry_window = my_canvas.create_window(220, 60, anchor="nw", window=width_entry)
height_entry_window = my_canvas.create_window(380, 60, anchor="nw", window=height_entry)
format_entry_window = my_canvas.create_window(640, 60, anchor="nw", window=format_entry)

root.mainloop()




## for resizer uncomment - the defenition is down
##root.bind("<Configure>", resizer)


### Bind the entry Boxes to the clear defenitions
##width_entry.bind("<Button-1>", entry_clear1)
##height_entry.bind("<Button-1>", entry_clear2)
##format_entry.bind("<Button-1>", entry_clear3)







'''
input_folder_entry = Entry(my_frame)
input_folder_entry.pack()

'''
#input_folder_label = my_canvas.create_text(100, 28, text="Input folder:", font=("Thoma", 20), fill="pink")
#input_folder_label = my_canvas.create_text(100, 28, text="Output folder:", font=("Thoma", 20), fill="pink")
#input_folder_label = my_canvas.create_text(100, 28, text="Input folder:", font=("Thoma", 20), fill="pink")


# for resizer uncomment
##def resizer(e):
##    global bg1, resized_bg, new_bg
##    # Open our image
##    bg1 = Image.open('buldog.gif')
##    # Resize the image
##    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
##    # Define our image again
##    new_bg = ImageTk.PhotoImage(resized_bg)
##    # add it back to  the Canvas
##    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
##    # Add the text back
##    my_canvas.create_text(507, 30, text="Universal Pictures Convertor", font=("Thoma", 40), fill="orange")
##

'''

input_folder_entry = Entry(my_frame)
input_folder_entry.pack()

input_folder_button = Button(my_frame, text="Select folder", command=select_input_folder)
input_folder_button.pack()

, command=select_input_folder)
'''


'''



def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, END)

def convert_to_format(input_folder, output_folder, format, width, height):
    for filename in os.listdir(input_folder):
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Resize image
            if width and height:
                img = img.resize((int(width), int(height)))
            elif width:
                wpercent = (int(width) / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((int(width), hsize))
            elif height:
                hpercent = (int(height) / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercent)))
                img = img.resize((wsize, int(height)))
            
            # Save in user-specified format
            if not filename.endswith('.' + format):
                filename = os.path.splitext(filename)[0] + "." + format
            img.save(os.path.join(output_folder, filename), format.upper())

def convert():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    format = format_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    convert_to_format(input_folder, output_folder, format, width, height,)







label = Label(root, image=bgpic)
label.place(x=0, y=0, relwidth=1, relheight=1)

my_frame = Frame(root, bg="white")
my_frame.pack(pady=20)

text1 = Label(root, text="Universal Pictures Convertor", font=("Helvetica", 20), fg="magenta", bg="white")
text1.pack(pady=20)

def select_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, END)
    input_folder_entry.insert(0, input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, END)

def convert_to_format(input_folder, output_folder, format, width, height):
    for filename in os.listdir(input_folder):
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Resize image
            if width and height:
                img = img.resize((int(width), int(height)))
            elif width:
                wpercent = (int(width) / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((int(width), hsize))
            elif height:
                hpercent = (int(height) / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercent)))
                img = img.resize((wsize, int(height)))
            
            # Save in user-specified format
            if not filename.endswith('.' + format):
                filename = os.path.splitext(filename)[0] + "." + format
            img.save(os.path.join(output_folder, filename), format.upper())

def convert():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    format = format_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    convert_to_format(input_folder, output_folder, format, width, height,)

Input folder:
input_folder_entry = Entry(my_frame)
input_folder_entry.pack()
 command=select_input_folder)


Output folder:
output_folder_entry = Entry(my_frame)
output_folder_entry.pack()
 command=select_output_folder)




format_label = Label(my_frame, text="Output format:")
format_label.pack()
format_entry = Entry(my_frame)
format_entry.pack()

width_label = Label(my_frame, text="Width:")
width_label.pack()
width_entry = Entry(my_frame)
width_entry.pack()

height_label = Label(my_frame, text="Height:")
height_label.pack()
height_entry = Entry(my_frame)
height_entry.pack()

convert_button = Button(my_frame, text="Convert", command=convert)
convert_button.pack()


root.mainloop()

############################################################


input_folder_label = Label(my_frame, text="Input folder:")
input_folder_label.pack()
input_folder_entry = Entry(my_frame)
input_folder_entry.pack()
input_folder_button = Button(my_frame, text="Select folder", command=select_input_folder)
input_folder_button.pack()

output_folder_label = Label(my_frame, text="Output folder:")
output_folder_label.pack()
output_folder_entry = Entry(my_frame)
output_folder_entry.pack()
output_folder_button = Button(my_frame, text="Select folder", command=select_output_folder)
output_folder_button.pack()

format_label = Label(my_frame, text="Output format:")
format_label.pack()
format_entry = Entry(my_frame)
format_entry.pack()

width_label = Label(my_frame, text="Width:")
width_label.pack()
width_entry = Entry(my_frame)
width_entry.pack()

height_label = Label(my_frame, text="Height:")
height_label.pack()
height_entry = Entry(my_frame)
height_entry.pack()

convert_button = Button(my_frame, text="Convert", command=convert)
convert_button.pack()
'''
