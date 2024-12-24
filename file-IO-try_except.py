# File I/O Handling in Python
# Reading and Writing Files in Python

# w - writing a file [Output Operation]
with open('text.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a text file.\n')
    file.write('This is a Python program.\n')

# r - reading a file [Input Operation]
with open('text.txt', 'r') as file:
    content = file.read()
    print(content)


# a - appending a file [Output Operation]
with open('text.txt', 'a') as file:
    file.write('This is a new line.\n')

# overwriting a file [Output Operation]
with open('text.txt', 'w') as file:
    file.write('This overwites the file.\n')

# Read, and Append Modes in Python
with open('text.txt', 'r+') as file:
    file.write('Hello, World!\n')
    file.write('This is a text file.\n')
    file.write('This is a Python program.\n')

    content = file.read()
    print("first content:", content)

    file.write('This is a new line.\n')

    content = file.read()
    print("second content:", content)

# Read as Text
with open('data.csv', 'rt') as file:
    content = file.read()
    print(content)


# Handling basic errors with try-except block

try:
    user_input = int(input("Enter a number: "))
    print("The number is:", user_input)
except:
    print("Invalid Input! Please enter a number.")


# Handling specific errors with try-except block
# File missing error

try:
    with open('text.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")



# Exercise 1:
# Write a Python program to read a file and display the content of the file.
# prompt the user to enter the file name.
# If the file does not exist, display an error message, and prompt them again.

