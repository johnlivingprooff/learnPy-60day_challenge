# Python Libraries

# Operating System library

import os
import datetime


# Examples of the OS library Methods

# Get the current working directory

os.getcwd() # returns the path to the CWD

# print(os.getcwd())

# list all the files & directories in the CWD

os.listdir('..')

# print(os.listdir('./.idea'))

# os.mkdir('./new_folder')
# os.remove()
# os.removedirs()
# os.rename()

# os.path()
os.path.exists('./')
# file_ = os.path.isfile('./data.csv')

# print(file_)
print(datetime.date.today())

'''

files/ - parent dir (..)
files/names/ - current dir (.)

'''



# Todays date

today = datetime.date.today()
print("Default format:", today)
print("Canged format:", today.strftime("%d, %m-%Y"))

