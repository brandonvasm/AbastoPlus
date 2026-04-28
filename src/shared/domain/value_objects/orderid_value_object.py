from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderItem:
    product_id: str
    quantity: int
    unit_price: Decimal

    def line_total(self) -> Decimal:
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if self.unit_price < 0:
            raise ValueError("Unit price cannot be negative")

        return self.quantity * self.unit_price