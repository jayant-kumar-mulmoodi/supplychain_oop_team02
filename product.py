
from exceptions import OutOfStockError

"""
Product class file

Step-by-step Instructions:
1. Define attributes:
   - product_id (int)
   - name (str)
   - price (float)
   - stock (int)
2. Add __init__, __str__, and update_stock methods.
3. Ensure stock >= 0 and price >= 0.
Hint: Use `max(0, stock)` to avoid negative stock values.
"""

class Product:
    def __init__(self, product_id, name, price, stock):
        # TODO: Initialize attributes
        # Hint: validate that price >= 0 and stock >= 0
        self.product_id=product_id
        self.name=name
        self.price=max(0,price)
        self.stock=max(0,stock)
        

    def __str__(self):
        # TODO: Return formatted string
        # Hint: f"Product[{self.product_id}] {self.name} - ${self.price}, Stock: {self.stock}"
        return f"Product[{self.product_id}] {self.name}- ${self.price},stock: {self.stock}"
    
    
    
   
    
    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock:
            raise OutOfStockError(f"Not enough stock for {self.name}! Available: {self.stock}")
        self.stock = max(0, self.stock + quantity)
        print(f"Updated stock of {self.name}: {self.stock}")