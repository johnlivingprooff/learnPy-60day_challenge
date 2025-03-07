# Debbuging

# def add_numbers(nums):
#     totl = 0
#     for num in nums:
#         # print(f'{num} is of data type: {type(num)}') # Debugging
#         totl += num
#     return totl

# list_of_numbers = [1, 2, 3, 4, 5, 6]
# result = add_numbers(list_of_numbers)
# print(f'The sum of {list_of_numbers} is {result}')

# Debugging 2
# import pdb

# def divide(a, b):
#     pdb.set_trace() 
#     '''Debugging comands for pdb.set_tace:
#     n -> next line / execute current line
#     l -> list code around affected area
#     c -> continue execution until next breakpoint
#     q / exit -> quit debugging session
#     p -> print variable value (p variable_name)
    
#     '''
#     return a / b

# result = divide(10, 0)
# print(result)


# Debugging 3

# def multiply(nums):
#     total = 1
#     for num in nums:
#         total *= num
#     return total

# list_of_numbers = [1, 2, 3, 4, 5, 6, '7']
# print(f'Original list: {list_of_numbers}')
# list_of_numbers = [num for num in list_of_numbers if type(num) == int or type(num) == float]
# print(f'Filtered list: {list_of_numbers}')
# try:
#     result = multiply(list_of_numbers)
# except Exception as e:
#     print(f'Error: {e}')
#     # list_of_numbers = [num for num in list_of_numbers if type(num) == int or type(num) == float]
# print(f'The product of {list_of_numbers} is {result}')

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(f'Error: {e}')
    
result = divide(10, 0)
print(result)