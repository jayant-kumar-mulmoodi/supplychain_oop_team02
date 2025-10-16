"""
Report class file

Step-by-step Instructions:
1. Add methods:
   - order_summary(order)
   - customer_orders(customer)
   - sales_report(orders)
2. Display clean formatted output.
Hint: Use loops and f-strings to format reports.
"""
from exceptions import CustomerNotFoundError
class Report:
    def order_summary(self, order):
        print("\n===== ORDER SUMMARY =====")
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {order.customer.name} ({order.customer.email})")
        print("Products:")
        
        total = 0
        for product, qty in order.products.items():
            print(f"  - {product.name} x {qty} = ₹{product.price * qty}")
            total += product.price * qty  
            print(f"Total: ₹{total}")

            
        print("--------------------------")
        print(f"Total: ₹{total}")
        print(f"Status: {order.status.value}")
        print("==========================")

    def customer_orders(self, customer):
        print("\n===== CUSTOMER ORDER HISTORY =====")
        if not customer.orders:
            raise CustomerNotFoundError(f"No orders found for customer {customer.name}")
        print(f"Customer: {customer.name}")
        print("Orders:")
        for order in customer.orders:
            print(f"  Order ID: {order.order_id} | Total: ₹{order.calculate_total()} | Status: {order.status.value}")
        print("=================================")

    def sales_report(self, orders):
        print("\n===== SALES REPORT =====")
        total_sales = sum(order.calculate_total() for order in orders)
        print(f"Total Orders: {len(orders)}")
        print(f"Total Revenue: ₹{total_sales}")
        print("========================")
