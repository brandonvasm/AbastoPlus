from dataclasses import dataclass
from .value_objects.money_value_object import Money


@dataclass(frozen=True)
class Product:
    id: str
    price: Money

    @staticmethod
    def create(product_id: str, price: float, currency: str) -> "Product":
        money = Money.create(price, currency)
        return Product(product_id, money)
    