import pytest
from shared.domain.value_objects.order import Order
from shared.domain.value_objects.order_status_value_object import OrderStatus
from shared.domain.value_objects.customerid_value_object import CustomerId


class TestOrder:

    class TestCreate:

        def test_creates_order_with_draft_status(self):
            customer_id = CustomerId.from_value("cust-123")

            order = Order.create(customer_id)

            assert order.status == OrderStatus.DRAFT
            assert order.customer_id == customer_id
            assert len(order.items) == 0