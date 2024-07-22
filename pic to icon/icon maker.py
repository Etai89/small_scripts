import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def load_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.ico")]
    )
    if file_path:
        img = Image.open(file_path)
        img_resized = img.resize((64, 64), Image.LANCZOS)
        save_image(img_resized)

def save_image(img):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".ico",
        filetypes=[("ICO files", "*.ico"), ("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")]
    )
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"Icon saved to {file_path}")

def create_gui():
    root = tk.Tk()
    root.title("Image to Icon Converter")

    load_button = tk.Button(root, text="Load Image", command=load_image)
    load_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
