'''
What is Inheritance?
Inheritance is a mechanism where a child class (derived class) can reuse and extend the functionality of a parent class (base class).

Example Analogy:

A Vehicle class can represent general features of vehicles (e.g., wheels, engine).
A Car class can inherit from Vehicle and add car-specific features (e.g., air conditioning, trunk).
'''

# Parent class
class Animal:

    # setter
    def __init__(self, bio_class, name):
        self.bio_class = bio_class
        self.name = name

    # GETTER
    def sound(self, snd):
        print(f'{self.name} makes {snd} sound')


# Derived class (child)
class Shark(Animal):
    def __init__(self, bio_class, name, water_body):
        super().__init__(bio_class, name)
        self.water_body = water_body

    def sound(self, snd):
        return super().sound(snd)
    

any_animal = Animal('mammal', 'monkey')

hammer_head = Shark('Amph', 'Tom', 'Ocean')

# any_animal.sound('monkey noise')
# hammer_head.sound('shark noise')


class Dog(Animal):
    def dog_type(self, dog_type):
        print(f'{self.name} is a {dog_type} dog, Bio class: {self.bio_class}')

dog1 = Dog('mammal', 'Bingo')

# dog1.dog_type('Domestic Dog')


class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner # protected attribute (cannot be edited directly)
        self.__balance = balance # private attribute (cannot be accessed directly)

    # getter method
    def get_balance(self):
        return self.__balance
    
    # setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print('You cannot set a negative balance')


user_one = BankAccount('John Doe', 5000)
user_one.set_balance(10000)
print(user_one.get_balance()) # 10000