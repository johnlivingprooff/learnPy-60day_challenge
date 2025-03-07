import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taker")
        self.root.geometry("300x300")

        # Create notebook and frame
        self.notebook = ttk.Notebook(self.root)
        self.frame = tk.Frame(self.notebook)

        # Create text area
        self.text_area = tk.Text(self.frame)
        self.text_area.pack(fill="both", expand=True)

        # Add frame to notebook
        self.notebook.add(self.frame, text="Note")

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Create file menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_note)
        self.file_menu.add_command(label="Save", command=self.save_note)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Pack notebook
        self.notebook.pack(fill="both", expand=True)

    def new_note(self):
        self.text_area.delete(1.0, tk.END)

    def save_note(self):
        note = self.text_area.get(1.0, tk.END)
        with open("note.txt", "w") as file:
            file.write(note)
        messagebox.showinfo("Note Saved", "Your note has been saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()



