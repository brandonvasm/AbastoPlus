import pytest
from shared.domain.value_objects.order import Order
from shared.domain.value_objects.order_status_value_object import OrderStatus
from shared.domain.value_objects.customerid_value_object import CustomerId
from shared.domain.order_mother import OrderMother
from shared.domain.value_objects.money_value_object import Money
from shared.domain.value_objects.quantity_value_object import Quantity

class TestOrder:

    class TestCreate:

        def test_creates_order_with_draft_status(self):
            customer_id = CustomerId.from_value("cust-123")
            order = OrderMother.create_draft_order()

            assert order.status == OrderStatus.DRAFT
            assert order.customer_id == customer_id
            assert len(order.items) == 0

    class TestAddItem:
        
        def test_adds_item_to_order(self):
            order = OrderMother.with_items(2)

            order.add_item(product_id="prod-5", quantity=2, unit_price=10.0, currency="USD")

            assert len(order.items) == 3
            item = order.items[2]
            assert item.product_id == "prod-5"
            assert item.quantity == Quantity.create(2)
            assert item.unit_price == Money(10.0, "USD")

        def test_throws_when_quantity_is_zero_or_negative(self):
            order = OrderMother.create_order()

            with pytest.raises(ValueError):
                order.add_item(product_id="prod-5", quantity=0, unit_price=10.0, currency="USD")

            with pytest.raises(ValueError):
                order.add_item(product_id="prod-5", quantity=-1, unit_price=10.0, currency="USD")

    class TestOrderItem:
        def test_increases_quantity_for_existing_item(self):
            order = OrderMother.with_items(2)

            order.add_item(product_id="prod-1", quantity=3, unit_price=10.0, currency="USD")

            assert len(order.items) == 2
            item = order.items[1]
            assert item.product_id == "prod-1"
            assert item.quantity == Quantity.create(4)
            assert item.unit_price == Money(10.0, "USD")

    class TestOrderStatus:
        def test_throws_when_order_is_cancelled(self):
            order = OrderMother.create_cancelled_order()

            with pytest.raises(ValueError):
                order.add_item(product_id="prod-5", quantity=2, unit_price=10.0, currency="USD")

