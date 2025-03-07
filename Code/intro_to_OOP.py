# Object Oriented Programming (OOP) in Python
# An Introduction:

"""
What is OOP?
A programming paradigm based on the concept of "objects," which bundle data (attributes) and behavior (methods).

Core OOP Concepts:
Classes: Blueprints for creating objects.
Objects: Instances of classes.
Attributes: Variables that hold object data.
Methods: Functions that define object behavior.

Analogy/Example:
A class is like a blueprint for a car (e.g., Car class).
An object is a specific car built using that blueprint (e.g., a red Toyota).
"""

# Example Class: Car

class Car:
    # Constructor or Initialising attribute
    def __init__(self, make=str, model=str, year=int):
        self.make = make # Attribute
        self.model = model # Attribute
        self.year = year # Attribute

    def drive(self):
        print(f'This {self.make} {self.model} is driving')

    def park(self):
        print()

    def reverse(self):
        pass

    def neutral(self):
        pass

    def show_info(self):
        print(f'This is a {self.make} {self.model}, made in {self.year}')

# creating car objects (instances of the car Class)
car_one = Car("Toyota", "Hilux", 2020) # created a car object
car_two = Car('KIA', 'Sol', 2013)

# calling car class methods

# car_one.show_info()
# car_two.drive()


# Table Class
class  BankAccount:
    '''
    
    '''
    def __init__(self, acct_name: str = "John Doe", acct_id: int = 10025, balance: float = 4563.23):
        self.acct_name = acct_name
        self.acct_id = acct_id
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        # self.balance += amount
        print("You new balance is: ", self.balance)

    def withdraw(self, amonut):
        self.balance -= amonut
        print("You new balance is: ", self.balance)


    def check_balance(self):
        print("You current balance is: ", self.balance)


    def show_acct_info(self):
        print(f'Acct Name: {self.acct_name}\nAcct ID: {self.acct_id}\nAccount Balance: {self.balance}')


person1 = BankAccount("Thomas", 1212, 50.00)

person1.show_acct_info()

person1.deposit(150)
person1.deposit(50)

person1.withdraw(45)

print(person1.acct_name)