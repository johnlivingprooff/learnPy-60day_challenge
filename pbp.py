import tkinter as tk
import pandas as pd
import os
import datetime
import numpy as np
import openpyxl
from tkinter import messagebox as mb
from tkinter import simpledialog as dlg
from tkinter import ttk



# ==================================================
# ** Main Window **
root = tk.Tk()
root.title('v2401s')
# Set window background color using RGB values
# root.configure(bg='#CCCCFF')  # light green color
root.columnconfigure(0, weight=1)

# ===============================================
# ** Main frame **
mf = tk.Frame(root)
mf.configure(background='#CCCCFF')  #
mf.grid(padx='5m', pady='5m', sticky=(tk.E + tk.W))
mf.columnconfigure(0, weight=1)
# -- Specify ttk styles
ypad = '1m'
xpad = '5m'
s = ttk.Style()
s.theme_use('alt')
# Section head label
s.configure('sh.TLabel',
            font=('Helvetica', 12, 'bold'),
            background='white',
            foreground='black',
            borderwidth=15,
            relief=tk.FLAT,
            )
# Other labels
s.configure('m.TLabel',
            font=('Helvetica', 12),
            background='white',
            borderwidth=10,
            relief=tk.FLAT
            )
# Buttons
s.configure('m.TButton',
            font=('Helvetica', 12),
            background='cyan',
            borderwidth=5,
            relief=tk.RAISED,
            )
# Entry
s.configure('m.TEntry',
            font=('Helvetica', 12),
            background='white',
            borderwidth=5,
            width=6,
            relief=tk.FLAT
            )
# Radio button
s.configure('m.TRadiobutton',
            background='white',
            borderwidth=5,
            width=14,
            relief=tk.FLAT
            )

# ---- Main title ------------
main_title = ttk.Label(mf, text='Prepare Builder and Trainee Payments',
                       style='m.TLabel', font=('Helvetica', 14, 'bold'))
grid_row = 0
main_title.grid(row=grid_row, column=0, pady=('10m', '5m'), padx='10m')

# ----------------------------------------------------------
# 1. Download installation data
# ----------------------------------------------------------
# -- Form selection (Install2024 or Install2024a)
form_label = ttk.Label(
    mf,
    text='Select Form to download and process:',
    style='m.TLabel'
)
grid_row += 1
form_label.grid(row=grid_row, column=0, padx=xpad, sticky=tk.W)

# Radio buttons
# Child frame to hold the radio buttons
download_choices = tk.Frame(mf)
download_choices.grid()
form_id_var = tk.StringVar(download_choices, 'Install2024a')
# Radio button - Install2024
rb = ttk.Radiobutton(
    download_choices,
    variable=form_id_var,
    value='Install2024',
    text='Install2024  ',
    style='m.TRadiobutton'
)
rb.grid(row=0)
# Radio button - Install2024a
rba = ttk.Radiobutton(
    download_choices,
    variable=form_id_var,
    value='Install2024a',
    text='Install2024a',
    style='m.TRadiobutton'
)
rba.grid(row=1)
# Place radiobuttons on mf
grid_row += 1
download_choices.grid(row=grid_row, column=0, sticky=tk.W, padx = xpad)

# -- Add button to download the data
download_btn = ttk.Button(mf, text=f'Download Installation data',
                          command=None, style='m.TButton')
grid_row += 1
download_btn.grid(row=grid_row, column=0, sticky=tk.W, pady=ypad, padx=xpad)

# ----------------------------------------------------------
# 2. Select the Program (Synod) to process
# ----------------------------------------------------------
synod_label = ttk.Label(mf, text='Select Program (Synod)', style='sh.TLabel')
grid_row += 1
synod_label.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)
# Radio buttons
synod_var = tk.StringVar(mf, 'All')
synod = 'All'
synod_name = 'All'
r1 = ttk.Radiobutton(mf, variable=synod_var, value=synod, text=synod_name, style='m.TRadiobutton')
grid_row += 1
r1.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)
synod = 'Liv'
synod_name = None
r2 = ttk.Radiobutton(mf, variable=synod_var, value=synod, text=synod_name, style='m.TRadiobutton')
grid_row += 1
r2.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)
synod = 'Nkh'
synod_name = None
r3 = ttk.Radiobutton(mf, variable=synod_var, value=synod, text=synod_name, style='m.TRadiobutton')
grid_row += 1
r3.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)
synod = 'Tan'
synod_name = None
r4 = ttk.Radiobutton(mf, variable=synod_var, value=synod, text=synod_name, style='m.TRadiobutton')
grid_row += 1
r4.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)
synod = 'Zam'
synod_name = None
r5 = ttk.Radiobutton(mf, variable=synod_var, value=synod, text=synod_name, style='m.TRadiobutton')
grid_row += 1
r5.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)

# ----------------------------------------------------------
# 2. Extract builder and trainee names
# ----------------------------------------------------------
# # -- Create the label for the Extract section
# extract_label = ttk.Label(mf, text='Extract Builder and Trainee names', style='sh.TLabel')
# grid_row += 1
# extract_label.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)

# -- Add button to extract the data
extract_btn = ttk.Button(mf, text=f'Extract Builder and Trainee names',
                         command=None, style='m.TButton')
grid_row += 1
extract_btn.grid(row=grid_row, column=0, sticky=tk.W, pady=ypad, padx=xpad)

# ----------------------------------------------------------
# 3. Compute builder and trainee payments
# ----------------------------------------------------------
# # -- Create the label for the payments section
# pay_label = ttk.Label(mf, text='Compute builder and trainee payments', style='sh.TLabel')
# grid_row += 1
# pay_label.grid(row=grid_row, column=0, pady=ypad, padx=xpad, sticky=tk.W)

# -- Add button to pay the data
pay_btn = ttk.Button(mf, text=f'Compute Builder and Trainee payments',
                     command=None, style='m.TButton')
grid_row += 1
pay_btn.grid(row=grid_row, column=0, sticky=tk.W, pady=('1m', '10m'), padx=xpad)

# ----------------------------------------------------------
# Log box
# -------------------------------------------------
# log_lbl = ttk.Label(mf, text='Program log', style='m.TLabel')
# log_lbl.grid(row=1, column=2, sticky=tk.W, pady=(ypad, '1m'), padx=xpad)
log_box = tk.Text(mf, width=50, height=35, padx='3m', pady='3m', wrap=tk.WORD)
log_box.grid(row=0, column=2, rowspan=13, sticky=tk.W + tk.E, pady=('1m', ypad), padx=xpad)

root.mainloop()
