# Inheritance + Encapsulation

# Parent class
class BankAccount:

    any_num = 1000 

    def __init__(self, owner, acct_id, balance):
        self.owner = owner
        self.acct_id = acct_id
        self.__balance = balance # Private Attribute 

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f'Dear {self.owner},\nYou have successfully deposited: {amount}')
        else:
            print('Sorry, You cannot deposit a negative amount')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Dear {self.owner},\nYou have successfully withdrawn: {amount}')
        else:
            print(f'Dear {self.owner},\nYou have Insufficient funds')

        
    def check_balance(self):
        print(f'Dear {self.owner},\nYour current balance is: {self.__balance}')

# Derived class
class CurrentAccount(BankAccount):
    
    overdraft = 1000 # class variable

    def withdraw(self, amount):
        # get current balance with BankAccount getter method
        if amount <= (self.get_balance() + self.overdraft):
            super().withdraw(amount)
            print(f'Dear {self.owner},\nYou have successfully withdrawn: {amount}')
        else:
            print(f'Dear {self.owner},\nYou have Insufficient funds')

    def print_any_num(self):
        print('Any number: ', BankAccount.any_num)

    def check_balance(self):
        # get current balance with BankAccount getter method
        current_balance = self.get_balance()
        print(f'Dear {self.owner},\nYour current balance is: {current_balance} and your overdraft is: {self.overdraft}')

class SavingsAccount(BankAccount):
    
    interest_rate = 0.5

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest) # use the parent class deposit method
        print(f"Dear {self.owner},\n {self.interest_rate * 100}% interest has been added to your account")

    def check_balance(self):
        # get current balance with BankAccount getter method
        current_balance = self.get_balance()
        print(f'Dear {self.owner},\nYour current balance is: {current_balance} and your interest rate is: {self.interest_rate * 100}%')


# creating objects
user_one = CurrentAccount('John Doe', 10025, 5000)
user_one.withdraw(5500)
user_one.check_balance()
user_one.print_any_num()

user_two = SavingsAccount('Jane Doe', 10026, 1000)
user_two.deposit(10000)
user_two.add_interest()
user_two.check_balance()