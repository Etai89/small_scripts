import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3

class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")

        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.open_button = ttk.Button(self.frame, text="Open Database", command=self.open_database)
        self.open_button.pack(pady=10)

        self.export_button = ttk.Button(self.frame, text="Export Data", command=self.export_data)
        self.export_button.pack(pady=10)

        self.tree = ttk.Treeview(self.frame)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.data = []  # To store the data for exporting

    def open_database(self):
        file_path = filedialog.askopenfilename(filetypes=[("SQLite files", "*.db *.sqlite3")])
        if file_path:
            self.load_database(file_path)

    def load_database(self, file_path):
        try:
            connection = sqlite3.connect(file_path)
            cursor = connection.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            self.data.clear()
            for table in tables:
                table_name = table[0]
                self.tree.insert('', 'end', text=table_name, values=("Table",))
                cursor.execute(f"SELECT * FROM {table_name}")
                columns = [description[0] for description in cursor.description]
                rows = cursor.fetchall()

                self.data.append(f"Table: {table_name}")
                self.data.append(", ".join(columns))
                for row in rows:
                    row_text = ", ".join(str(value) for value in row)
                    self.tree.insert('', 'end', text=row_text, values=(table_name,))
                    self.data.append(row_text)
                self.data.append("")

            connection.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def export_data(self):
        if not self.data:
            messagebox.showwarning("Export Warning", "No data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    for line in self.data:
                        file.write(line + "\n")
                messagebox.showinfo("Export Success", "Data exported successfully.")
            except IOError as e:
                messagebox.showerror("Export Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseViewer(root)
    root.mainloop()
