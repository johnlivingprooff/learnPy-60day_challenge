# ================================
# Day 1: Introduction to Python
# ================================

# 1. Hello, World! (Your first Python program)
print("Hello, World!")

# 2. Variables and their basic usage
print("\n--- Variables ---")
greeting = "Welcome to Python Programming!"
print(greeting)

# 3. Basic arithmetic operations
print("\n--- Arithmetic Operations ---")
a = 10
b = 5
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")

# Challenge: Modify the values of `a` and `b` and re-run the program
# a = 20
# b = 10

# 4. Using input to make the program interactive
print("\n--- User Input ---")
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

# 5. Combining strings with variables
print("\n--- String Manipulation ---")
age = input("How old are you? ")
print(f"{name}, you are {age} years old.")

# Challenge: Ask the user for their favorite number and print its square
# favorite_number = int(input("What is your favorite number? "))
# print(f"The square of {favorite_number} is {favorite_number ** 2}")

# ================================
# Day 2: Variables and Data Types
# ================================

# 6. Different data types
print("\n--- Data Types ---")
integer_var = 42  # Integer
float_var = 3.14  # Float
string_var = "Python is fun!"  # String
boolean_var = True  # Boolean
list_var = ["apple", "banana", "cherry"]  # List

print(f"Integer: {integer_var}")
print(f"Float: {float_var}")
print(f"String: {string_var}")
print(f"Boolean: {boolean_var}")
print(f"List: {list_var}")

# 7. Updating variables
print("\n--- Updating Variables ---")
count = 10
print(f"Initial Count: {count}")
count = count + 5
print(f"Updated Count: {count}")

# Challenge: Double the count and print the new value
# count = count * 2
# print(f"Doubled Count: {count}")

# 8. A practical example: Bookstore information
print("\n--- Practical Example: Bookstore ---")
title = "The Great Gatsby"
author = "F. Scott Fitzgerald"
price = 15.99
is_available = True

print(f"Title: {title}")
print(f"Author: {author}")
print(f"Price: ${price}")
print(f"Available: {is_available}")

# 9. Basic arithmetic with variables
print("\n--- Area of a Rectangle ---")
length = 10
width = 5
area = length * width
print(f"The area of a rectangle with length {length} and width {width} is {area}.")

# Challenge: Modify the length and width to calculate a new area
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# print(f"The new area is {area}")

# 10. Error handling
print("\n--- Error Handling ---")
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Oops! That's not a valid number.")

# ================================
# Summary and Final Challenge
# ================================
print("\n--- Summary Challenge ---")

# Task: Create a simple program that stores and displays a user's profile
name = input("What is your name? ")
age = int(input("How old are you? "))
favorite_color = input("What is your favorite color? ")

print("\nHere is your profile:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Color: {favorite_color}")

# End of the script. Continue exploring Python!
