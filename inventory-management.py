'''
Inventory Management System.

Solution: Three Object classes that would represent 3 different Operations / Items that would be involved with this system.

Three Classes:
- Product Class, all the items that are in the Warehouse would be instances of this class
- Inventory Class - This keeps track of multiple items/product-instances in the warehouse
- UserInterface Class; provides a user-friendly interface.

'''

import os
import matplotlib.pyplot as plt
import requests
import pandas
import json

class Product:

    def __init__(self, name, qty, metric, price, category):
        self.name = name
        self.qty = qty
        self.metric = metric
        self.price = price
        self.category = category
        self.stock_value = price * qty

    def update_qty(self, new_qty):
        if new_qty < 0:
            print('Quantity cannot be less than 0')
        if new_qty >= 1:
            self.qty = new_qty
            print(f'Quantity for {self.name} been updated to {self.qty}{self.metric}')

    def to_dict(self):
        """ Converting the product details into a dictionary formated JSON """
        return {
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'qty': self.qty
        }

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price} / {self.metric} | Stock: {self.qty}{self.metric}, Stock Value: {self.stock_value}"


class Inventory:
    def __init__(self):
        self.products = []

        def add_product(self, product):
            """ Adds a product to the product list """
            self.products.append(product)
            print(f"Product: {product.name} successfully added")
        
        def remove_product(self, product_name):
            """ Remove product from product list """
            # self.products = [ p for p in self.products if p.name.lower() != product_name.lower() ]
            # print(f"Product: {product_name} removed added")

            for product in self.products:
                if product.name.lower() == product_name.lower():
                    self.products.remove(product)
                    print(f"Product: {product_name} removed")
                    return
                

        def update_stock(self, product_name, new_qty):
            for product in self.products:
                if product.name.lower() == product_name.lower():
                    product.update_qty(new_qty)
                    print(f"Product: {product_name} stock updated to {new_qty}")
                    return
            print(f"Product: {product_name} not found")

        def display_inventory(self):

            if not self.products:
                print('No products in the inventory')
                return
            
            for product in self.products:
                print(product)

        def save_to_file(self):
            """Saving the inventory to a JSON File"""
            with open("inventory.json", "w") as f:
                json.dump([p.to_dict() for p in self.products], f, indent=4)
            print("Inventory saved to inventory.json successfully")

        def load_from_file(self):
            """Get JSON formatted data from the inventory file"""
            if os.path.exists("inventory.json"):
                with open("inventory.json", "r") as f:
                    data = json.load(f)
                    self.products = [Product(**product) for product in data]
                print("Inventory loaded from inventory.json successfully")

            else:
                print("No inventory file found")

class UserInterface:

    def __init__(self):
        self.inventory = Inventory()
        self.inventory.load_from_file()

    def display_menu(self):
        while True:
            print("\n📦 Inventory Management System")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Update Stock")
            print("4. Display Inventory")
            print("5. Save Inventory")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                category = input("Enter product category: ")
                qty = int(input("Enter product quantity: "))
                metric = input("Enter product metric: ")

                new_product = Product(name, qty, metric, price, category)
                self.inventory.add_product(new_product)
                self.inventory.save_to_file() # Save the inventory to the file


            elif choice == '2':
                product_name = input("Enter product name: ")
                self.inventory.remove_product(product_name)
                

        

# .. - parent_directory
# . - current directory

                
       

# Object
obj1 = Product('Rice', 50, 'kg', 2500, 'food')


