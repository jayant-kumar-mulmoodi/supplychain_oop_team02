from exceptions import InvalidOrderOperationError
from order_status import OrderStatus
"""
Order class file

Step-by-step Instructions:
1. Define attributes:
   - order_id (int)
   - customer (Customer object)
   - products (dict {Product: qty})
   - status (OrderStatus enum)
2. Add methods:
   - add_product(product, qty)
   - remove_product(product_id)
   - calculate_total()
   - update_status(new_status)
"""


        
class Order:
    def __init__(self, order_id="", customer=None):
        self.order_id = order_id
        self.customer = customer
        self.products = {}
        self.status = OrderStatus.PENDING
        
        
        
    def add_product(self, product, qty):
        self.products[product] = self.products.get(product, 0) + qty
        print(f"Added {qty} of {product.name} to Order {self.order_id}")

        
        


    def remove_product(self, product_id):
        for prod in list(self.products.keys()):
            if prod.product_id == product_id:
                del self.products[prod]
                print(f"Removed product: {prod.name} from Order {self.order_id}")
                return
        raise InvalidOrderOperationError(f"Product ID {product_id} not found in Order {self.order_id}")

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.products.items())

    def update_status(self, new_status):
        if not isinstance(new_status, OrderStatus):
            raise InvalidOrderOperationError("Invalid status type!")
        if self.status == OrderStatus.DELIVERED and new_status == OrderStatus.CANCELLED:
            raise InvalidOrderOperationError(f"Cannot cancel Order {self.order_id} — already delivered!")
        self.status = new_status
        print(f"Order {self.order_id} updated to {self.status.value}")