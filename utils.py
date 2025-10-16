"""
Helper functions file

Step-by-step Instructions:
1. Implement:
   - validate_price(price)
   - validate_quantity(qty)
2. Add ID generator (e.g., order_id).
Hint: Use itertools.count() or uuid.uuid4() for unique IDs
"""

import itertools

_id_counter = itertools.count(1)

def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return True

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return True

def generate_id():
    return next(_id_counter)
