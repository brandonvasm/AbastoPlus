from .value_objects.order import Order
from .value_objects.customerid_value_object import CustomerId
from .value_objects.order_status_value_object import OrderStatus
from .value_objects.orderid_value_object import OrderItem
from .value_objects.money_value_object import Money
from .value_objects.quantity_value_object import Quantity


class OrderMother:
    @staticmethod
    def create_order() -> Order:
        return Order.create(
            customer_id=CustomerId.from_value("cust-123"),
            status=OrderStatus.CONFIRMED,
        )
    
    @staticmethod
    def create_draft_order() -> Order:
        return Order.create(
            customer_id=CustomerId.from_value("cust-123"),
        )
    
    @staticmethod
    def create_cancelled_order() -> Order:
        return Order.create(
            customer_id=CustomerId.from_value("cust-123"),
            status=OrderStatus.CANCELLED,
        )
    
    @staticmethod
    def with_items(n: int) -> Order:
        return Order.create(
            customer_id=CustomerId.from_value("cust-123"),
            status=OrderStatus.CONFIRMED,
            items=[OrderItem(product_id=f"prod-{i}", quantity=Quantity.create(1), unit_price=Money(10.0, "USD")) for i in range(n)]
        )
    