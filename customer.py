from exceptions import CustomerNotFoundError
"""
Customer class file

Step-by-step Instructions:
1. Define attributes:
   - customer_id (int)
   - name (str)
   - email (str)
   - orders (list of Order objects)
2. Add __init__, add_order, get_order_history methods.
Hint: Use a list to store order references.
"""

class Customer:
    def __init__(self, customer_id, name, email):
        # TODO: Initialize attributes
        # Hint: self.orders = []
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.orders=[]
        

    def add_order(self, order):
        # TODO: Append order to list
        # Hint: self.orders.append(order)
        self.orders.append(order)


    def get_order_history(self):
        # TODO: Return order details
        # Hint: Loop through self.orders and return summaries
        if not self.orders:
            # raise custom exception when customer has no orders
            raise CustomerNotFoundError(f"No orders found for customer {self.name} (ID: {self.customer_id})")
        for i in self.orders:
            return f"customer id is {i.customer_id} and name is {i.name} and email is the {i.emial} and {i.orders}"
        