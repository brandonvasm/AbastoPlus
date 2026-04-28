from dataclasses import dataclass
from decimal import Decimal
from .money_value_object import Money
from .quantity_value_object import Quantity

class OrderItem:
    product_id: str
    quantity: Quantity
    unit_price: Money

    def __init__(self, product_id: str, quantity: Quantity, unit_price: Money):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

    def line_total(self) -> Decimal:
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if self.unit_price < 0:
            raise ValueError("Unit price cannot be negative")

        return self.quantity * self.unit_price.amount
    