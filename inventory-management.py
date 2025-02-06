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
            self.products = [ p for p in self.products if p.name.lower() != product_name.lower() ]
            print(f"Product: {product_name} removed added")

        def update_stock(self, product_name, new_qty):
            for product in self.products:
                if product.name.lower() == product_name.lower():
                    product.update_qty(new_qty)
                    print(f"Product: {product_name} stock updated to {new_qty}")
                    return
            print(f"Product: {product_name} not found")



                
       

# Object
obj1 = Product('Rice', 50, 'kg', 2500, 'food')


