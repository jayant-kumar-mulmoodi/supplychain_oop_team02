"""
Main Driver File: Order Management System

Features:
1. Create orders for customers
2. Add/remove products
3. View order summary
4. View customer order history
5. Handle errors gracefully
"""

from product import Product
from customer import Customer
from order import Order
from report import Report
from exceptions import OutOfStockError, InvalidOrderOperationError, CustomerNotFoundError
from utils import validate_price, validate_quantity, generate_id


def main():
    # Sample Data
    p1 = Product(101, "Laptop", 50000, 10)
    p2 = Product(102, "Mouse", 500, 50)
    p3 = Product(103, "Keyboard", 1200, 20)
    products = [p1, p2, p3]

    c1 = Customer(1, "Amit Kumar", "bittu@example.com")
    c2 = Customer(2, "Riya Singh", "riya@example.com")
    customers = [c1, c2]

    orders = []
    report = Report()

    while True:
        print("\n=== ORDER MANAGEMENT SYSTEM ===")
        print("1. Create Order")
        print("2. Add Product to Order")
        print("3. Remove Product from Order")
        print("4. View Order Summary")
        print("5. View Customer Order History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            # 1. Create Order
            if choice == "1":
                cust_id = int(input("Enter Customer ID: "))
                customer = next((c for c in customers if c.customer_id == cust_id), None)
                if not customer:
                    raise CustomerNotFoundError(f"Customer with ID {cust_id} not found!")

                order_id = generate_id()
                order = Order(order_id, customer)
                orders.append(order)
                customer.add_order(order)
                print(f"Order {order_id} created for {customer.name}.")

            # 2. Add Product to Order
            elif choice == "2":
                order_id = int(input("Enter Order ID: "))
                order = next((o for o in orders if o.order_id == order_id), None)
                if not order:
                    print("Order not found!")
                    continue

                prod_id = int(input("Enter Product ID to add: "))
                product = next((p for p in products if p.product_id == prod_id), None)
                if not product:
                    print("Product not found!")
                    continue

                qty = int(input("Enter quantity: "))
                validate_quantity(qty)

                if qty > product.stock:
                    raise OutOfStockError(f"Not enough stock for {product.name}. Available: {product.stock}")

                product.update_stock(-qty)
                order.add_product(product, qty)
                print(f"Added {qty} x {product.name} to Order {order_id}.")

            # 3. Remove Product from Order
            elif choice == "3":
                order_id = int(input("Enter Order ID: "))
                order = next((o for o in orders if o.order_id == order_id), None)
                if not order:
                    print("Order not found!")
                    continue

                prod_id = int(input("Enter Product ID to remove: "))
                order.remove_product(prod_id)
                print(f"Product removed from Order {order_id}.")

            # 4. View Order Summary
            elif choice == "4":
                order_id = int(input("Enter Order ID: "))
                order = next((o for o in orders if o.order_id == order_id), None)
                if not order:
                    print("Order not found!")
                    continue

                report.order_summary(order)

            # 5. View Customer Order History
            elif choice == "5":
                cust_id = int(input("Enter Customer ID: "))
                customer = next((c for c in customers if c.customer_id == cust_id), None)
                if not customer:
                    raise CustomerNotFoundError(f"Customer with ID {cust_id} not found!")

                report.customer_orders(customer)

            # 6. Exit
            elif choice == "6":
                print("Exiting the system... Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 6.")

        except (OutOfStockError, InvalidOrderOperationError, CustomerNotFoundError) as e:
            print("Error:", e)
        except ValueError:
            print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()
