# Loops, Conditional Statements, Functions

list_of_numbers = [1, 2, 3, 4, 5]

list_of_chars = ['a', 'b', 'c', 'd', 'e']

list_of_str = ['one', 'two', 'three', 'four']

list_of_str[3] # is accessing 'four'

# print(list_of_str[3])

# Multiply each Item in the list by 10 and add all of them up
total = 0

# For iterating through a list of items
for num in list_of_numbers:
    total = total + (num * 10)
    
print(total)

# range()

print('----------------------------------------')
print('range()')

for i in range(10): # 0 - 9
    print(i)

print('----------------------------------------')
print('range(10, 50) | Find the even numbers within the range')

for i in range(10, 50): # 10, 11, ..., 49
    if i % 2 == 0:
        print(i)

# While loop

print('While Loop')

count = 0

while count < 10:
    print('count:', count)
    count += 1

print()
print('----------------------------------------')
print()

i = 0
while i < 50 and i % 2 == 0:
    print('value:', i)
    i += 1

# Nested if-statement

while i < 50:
    if i % 2 == 0:
        print('value:', i)
    i += 1

print()
print('----------------------------------------')
print()

i = 45
if i < 50:
    if i % 2 == 0: # is i a even number
        print('i is even:', i)
    print('i is odd:')
print(f'i is {i}')

print()
print("Loop Exercises")
print()

start = int(input('Input a Start number'))
end = int(input('Input the last number in the range'))
current = start
sum_even = 0

while current <= end:
    if current % 2 == 0:
        sum_even += current
    current+=1 

print(f'the sum of even numbers between {start} and {end} is {sum_even}')

# Calculating Factorials

fn = int(input("Let's find the factorial of your number\nWrite your number: "))
factorial = 1
while fn > 0:
    factorial *= fn
    fn -= 1
print(f'your factorial is {factorial}')
