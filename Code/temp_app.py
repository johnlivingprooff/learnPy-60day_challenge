import tkinter as tk

def convert_temp():
    celsius = float(entry.get())  # Get input value
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}°F")  # Update label

# Create GUI window
root = tk.Tk()
root.title("Temperature Converter")

# Input field
entry_label = tk.Label(root, text="Enter Temperature in Celsius:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.pack()

# Result display
result_label = tk.Label(root, text="Fahrenheit: --°F", font=("Arial", 12))
result_label.pack()

# Run the GUI loop
root.mainloop()
