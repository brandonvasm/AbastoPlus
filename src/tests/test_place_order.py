import pytest

from shared.application.place_order_handler import PlaceOrderHandler, PlaceOrderCommand
from shared.infraestructure.order_container import OrderContainer
from shared.domain.product import Product


class TestPlaceOrderHandler:

    def setup_method(self):
        self.order_container = OrderContainer()
        self.order_repo = self.order_container.order_repository()
        self.product_repo = self.order_container.product_repository()
        self.handler = self.order_container.order_handler()

    def test_creates_order_with_items_and_saves(self):
        self.product_repo.add_product(Product.create("prod-1", 50.2, "GTQ"))
        self.product_repo.add_product(Product.create("prod-2", 20.0, "GTQ"))

        command: PlaceOrderCommand = {
            "customer_id": "cust-123",
            "items": [
                {"product_id": "prod-1", "quantity": 2},
                {"product_id": "prod-2", "quantity": 1},
            ]
        }
    
        order_id = self.handler.handle(command)

        assert order_id is not None

        saved_order = self.order_repo.find_by_id(order_id)
        assert saved_order is not None
        