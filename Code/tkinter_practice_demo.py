import tkinter as tk

# Create a window
root = tk.Tk()
root.title("Simple Tkinter Window")

# Create a Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=10)

# Run the GUI loop
root.mainloop()
