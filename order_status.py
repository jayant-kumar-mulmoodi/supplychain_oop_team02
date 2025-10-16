"""
An Enum is a set of symbolic names bound to unique values. They are similar to global variables, but they offer a more useful repr(), grouping, type-safety, and a few other features.

They are most useful when you have a variable that can take one of a limited selection of values. For example, the days of the week

link : https://docs.python.org/3/howto/enum.html

Order status file

Step-by-step Instructions:
1. Use Enum for order statuses.
2. Define statuses:
   - PENDING
   - SHIPPED
   - DELIVERED
   - CANCELLED
Hint: Import Enum → from enum import Enum



"""

from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
