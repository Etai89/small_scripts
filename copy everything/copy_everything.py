import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def copy_files(src_folder, dst_folder, extensions):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in extensions or '*' in extensions:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(dst_folder, file)
                shutil.copy(src_path, dst_path)

def select_src_folder():
    folder_path = filedialog.askdirectory()
    src_folder.set(folder_path)

def select_dst_folder():
    folder_path = filedialog.askdirectory()
    dst_folder.set(folder_path)

def select_extensions(*args):
    extensions = extensions_listbox.curselection()
    extensions = [extensions_listbox.get(i) for i in extensions]
    extensions = ['*' if 'All Files' in extensions else ext for ext in extensions]
    extensions_var.set(extensions)

root = tk.Tk()
root.title("File Copier")

src_folder = tk.StringVar()
dst_folder = tk.StringVar()

extensions_var = tk.StringVar()
extensions_var.set(['*'])

extensions_list = [
    'All Files',
    '.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.odg',
    '.rtf', '.csv', '.html', '.htm', '.xml', '.json', '.yaml', '.md', '.py', '.cpp', '.h', '.java', '.cs', '.js',
    '.ts', '.php', '.css', '.scss', '.less', '.sass', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.ico',
    '.svg', '.mp3', '.wav', '.ogg', '.mp4', '.mov', '.avi', '.mkv', '.zip', '.tar', '.gz', '.rar', '.7z', '.exe',
    '.msi', '.bat', '.sh', '.sql', '.xml', '.json', '.yml', '.yaml', '.ini', '.cfg', '.conf', '.log', '.bak', '.swp',
    '.swo', '.psd', '.ai', '.eps', '.svgz', '.tga', '.dds', '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx',
    '.odt', '.ods', '.odp', '.odg', '.wpd', '.msg', '.eml', '.mbox', '.pst', '.db', '.mdb', '.accdb', '.sqlitedb', '.bak',
    '.tmp', '.swf', '.flv', '.mpg', '.mpeg', '.ps', '.eps', '.ai', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.srf',
    '.bay', '.raf', '.iso', '.img', '.bin', '.cue', '.vob', '.ifo', '.bup', '.dmg', '.toast', '.deb', '.rpm', '.jar',
    '.java', '.class', '.war', '.ear', '.html', '.xhtml', '.asp', '.aspx', '.jsp', '.jspx', '.php4', '.php3', '.phtml',
    '.inc', '.cfg', '.conf', '.htaccess', '.htpasswd', '.log', '.txt', '.README', '.md', '.nfo', '.ini', '.json',
    '.js', '.css', '.dll', '.sys'
]

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky="nsew")

ttk.Label(frame, text="Source Folder:").grid(column=0, row=0, sticky="w")
ttk.Entry(frame, textvariable=src_folder).grid(column=1, row=0)
ttk.Button(frame, text="Browse", command=select_src_folder).grid(column=2, row=0)

ttk.Label(frame, text="Destination Folder:").grid(column=0, row=1, sticky="w")
ttk.Entry(frame, textvariable=dst_folder).grid(column=1, row=1)
ttk.Button(frame, text="Browse", command=select_dst_folder).grid(column=2, row=1)

ttk.Label(frame, text="Extensions:").grid(column=0, row=2, sticky="w")
extensions_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
extensions_listbox.grid(column=1, row=2, sticky="w")
extensions_listbox.insert(tk.END, *extensions_list)

extensions_var.trace('w', select_extensions)

ttk.Button(frame, text="Copy Files", command=lambda: copy_files(src_folder.get(), dst_folder.get(), extensions_var.get())).grid(column=1, row=8)

root.mainloop()
