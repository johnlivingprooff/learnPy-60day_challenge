"""
Building a GUI Budget/Expenses tracker.

Functions/Main Logic:
    - Add expenses
    - View expenses
    - Save expenses to a database
    - Load expenses from a database

GUI Elements: (we're building a simple Interface)
    - Title of the Application
    - Entry field for the expense category
    - Entry field for the amount
    - Button to add expenses
    - Button to view expenses
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Initialize the Database
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS expenses ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            category TEXT, 
            amount REAL)''')
conn.commit()

# Function to add expenses
def add_expenses():
    category = category_get.get()
    amount = amount_get.get()

    if not category or not amount:
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return
    
    cur.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()

    messagebox.showinfo("Success", "Expense added successfully")
    category_get.delete(0, tk.END)
    amount_get.delete(0, tk.END)

# Function to view expenses 
def view_expenses():
    cur.execute("SELECT category, amount FROM expenses")
    recs = cur.fetchall()

    exp_window = tk.Toplevel(root)
    exp_window.title("Expenses")

    # Display the Expenses as a Table (Creating Columns)
    tk.Label(exp_window, text="Category", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    tk.Label(exp_window, text="Amount", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

    # Display the Expenses as a Table (Populating the Table)
    for i , (category, amount) in enumerate(recs, start=1):
        tk.Label(exp_window, text=category, width=15).grid(row=i, column=0, padx=10, pady=10)
        tk.Label(exp_window, text=f"{amount:,.2f}", width=15).grid(row=i, column=1, padx=10, pady=10)

def visualise_data():
    cur.execute("SELECT category, amount FROM expenses")
    recs = cur.fetchall()

    if not recs:
        messagebox.showerror("Error", "No expenses to visualise")
        return
    
    categories = [row[0] for row in recs]
    amounts = [row[1] for row in recs]

    # [ # recs
    #     ('food', 'morgage', 'rent'), # = Categories
    #     (1000, 2000, 3000), # = Amounts
    # ]

    plt.figure(figsize=(10, 5))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow'])
    plt.title("Expenses Distribution")
    plt.show()


# Build the GUI
root = tk.Tk()
root.title("Budget Tracker")

tk.Label(root, text="Budget/Expence Tracker", font=("Arial", 16)).pack(pady=10)

# User Inputs
tk.Label(root, text="Category").pack()
category_get = tk.Entry(root)
category_get.pack()

tk.Label(root, text="Amount (MWK)").pack()
amount_get = tk.Entry(root)
amount_get.pack()

# Buttons
tk.Button(root, text="Add Expense", command=add_expenses).pack(pady=10)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=10)
tk.Button(root, text="Visualise Expenses", command=visualise_data).pack(pady=10)


root.mainloop()
conn.close()

# Creating a Windows Executable file:

'''
pyinstaller --onefile --hidden-import PIL --hidden-import pillow --add-data "J:\Documents\CODE\Practice\Python\imgs\icon.png;imgs" --icon=.\imgs\icon.ico --windowed budget_tracker_practice.py    
'''