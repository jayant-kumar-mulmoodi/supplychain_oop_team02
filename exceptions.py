"""
Custom exceptions for order management
Hint: Use them when invalid operations happen
"""

class OutOfStockError(Exception):
    """Raised when product stock is insufficient"""
    pass

class InvalidOrderOperationError(Exception):
    """Raised for invalid order operations"""
    pass

class CustomerNotFoundError(Exception):
    """Raised when customer is not found"""
    pass
