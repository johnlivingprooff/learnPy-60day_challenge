import tkinter as tk

# Demo GUI
window = tk.Tk()
window.title("Demo GUI") # Title of the window 

# Create a label widget
label = tk.Label(window, text="60 Days Of Py")
label.pack() # Add the label to the window

# Run the GUI
window.mainloop() # loops to keep the window open


'''
✅ Key Points:

Tk() creates a window.
Label() creates text inside the window.
pack() places widgets inside the window.
mainloop() keeps the window running.

'''