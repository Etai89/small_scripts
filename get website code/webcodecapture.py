import tkinter as tk
from tkinter import *
import urllib.request
from tkinter import filedialog

class Browser:
    def __init__(self, master):
        self.master = master
        self.master.title("Website Code Capture")
        master.geometry("900x700")
        master.minsize(800, 700)
        master.maxsize(800, 700)
##        master.iconbitmap("fet.ico")
        
        my_label = Label(root, text="             website code sniffer              ", font=("Helvetika", 40), bg='grey', fg='darkred')
        my_label.pack()
        
        my_label = Label(root, text="                                                                 Enter URL :                                                              ", font=("Helvetika", 15), bg='grey', fg='purple')
        my_label.pack()

        
        self.url_entry = tk.Entry(self.master, width=70 , font=("Arial", 15), bg='lightblue', fg='red')
        self.url_entry.pack(pady=2)
        
        self.go_button = tk.Button(self.master, text="                                                   Go                                                    ",  font=("Arial", 18), bg='grey', fg='lime',command=self.go)
        self.go_button.pack(pady=2)

        self.back_button = tk.Button(self.master, text="                                                 Back                                                 ", font=("Arial", 15), bg='grey', fg='lime', command=self.back)
        #self.back_button.pack(pady=2)
        
        self.forward_button = tk.Button(self.master, text="                                         Forward                                        ", font=("Arial", 15), bg='grey', fg='lime', command=self.forward)
        #self.forward_button.pack(pady=2)

        self.save_button = tk.Button(self.master, text="                                                            Save                                                           ", font=("Arial", 15), bg='grey', fg='lime', command=self.save_file)
        self.save_button.pack(pady=2)

        self.text = tk.Text(self.master, height=20, width=70, font=("Arial", 15), bg='lightblue', fg='red')
        self.text.pack(pady=2)

        
        
        self.history = []
        self.current = 0

    def save_file(self):
        file = filedialog.asksaveasfile(initialdir="",
                                                                    defaultextension='.txt',
                                                                    filetypes=[
                                                                        ("Text file", ".txt"),
                                                                        ("HTML file", ".html"),
                                                                        ("All files", ".*")
                                                                        ])
        if file is None:
            return
        filetext = str(self.text.get(1.0, END))
        file.write(filetext)
        file.close()
                 
    def go(self):
        url = self.url_entry.get()
        self.history.append(url)
        self.current += 1
        with urllib.request.urlopen(url) as response:
            html = response.read()
            
            self.text.insert(tk.END, html.decode("utf-8"))
        
    def back(self):
        if self.current > 0:
            self.current -= 1
            with urllib.request.urlopen(self.history[self.current]) as response:
                html = response.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, html.decode("utf-8"))
        
    def forward(self):
        if self.current + 1 < len(self.history):
            self.current += 1
            with urllib.request.urlopen(self.history[self.current]) as response:
                html = response.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, html.decode("utf-8"))
            

root = tk.Tk()
browser = Browser(root)
root.mainloop()
