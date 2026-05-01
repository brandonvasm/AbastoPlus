from shared.domain.value_objects.customerid_value_object import CustomerId
from shared.domain.value_objects.order import Order

from shared.domain.repositories.order_repository import OrderRepository
from shared.domain.repositories.product_repository import ProductRepository

from typing import TypedDict

class PlaceOrderCommand(TypedDict):
    customer_id: str
    items: list

class PlaceOrderHandler:

    def __init__(self, order_repo: OrderRepository, product_repo: ProductRepository):
        self.order_repo = order_repo
        self.product_repo = product_repo

    def handle(self, command: PlaceOrderCommand) -> str:
        customer_id = CustomerId.from_value(command["customer_id"])

        order = Order.create(customer_id)

        for item in command["items"]:
            product = self.product_repo.find_by_id(item["product_id"])

            if product is None:
                raise ValueError("Product not found")

            order.add_item(
                product_id=product.id,
                quantity=item["quantity"],
                unit_price=product.price.amount,
                currency=product.price.currency
            )

        self.order_repo.save(order)

        return order.id
    