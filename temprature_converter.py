import tkinter as tk

# Create a method to convert temprature
def convert_temp():
    celsius = entry.get()
    fahrenheit = (9/5) * float(celsius) + 32
    answer_label.config(text=f"The temperature in Fahrenheit is: {fahrenheit}")

# create a window
root = tk.Tk()
root.title("Temprature Converter")


# Create a label widget
title_label = tk.Label(root, text="Temprature Converter", font=("Arial", 14))
title_label.pack(pady=25)

# Create an entry widget
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Convert", font=("Arial", 14), command=convert_temp)
button.pack(pady=10, padx=10)

# Create a aswer label widget
answer_label = tk.Label(root, text="The temperature in Fahrenheit is: --", font=("Arial", 14))
answer_label.pack(pady=50, padx=25)

# Run the GUI
root.mainloop() # loops to keep the window open

