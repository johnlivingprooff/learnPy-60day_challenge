# a basic calculator (supports addition, subtraction,  multiplication, and division). 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == '__main__':
    select_operator = input("Select operator (+, -, *, /): ")
    
    while True:
        if select_operator in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if select_operator == '+':
                # print(num1, "+", num2, "=", add(num1, num2))
                addition = add(num1, num2)
                print(f"{num1} + {num2} = {addition}") # 5 + 6 = 11
                break

            elif select_operator == '-':
                sub = subtract(num1, num2)
                print(f"{num1} - {num2} = {sub}")
                break

            elif select_operator == '*':
                mul = multiply(num1, num2)
                print(f"{num1} * {num2} = {mul}")
                break

            elif select_operator == '/':
                div = divide(num1, num2)
                print(f"{num1} / {num2} = {div}")
                break
                
        else:
            print("Invalid operator, please input correct operator from this list.\n(+, -, *, /)")
            select_operator = input("Select operator (+, -, *, /): ")


