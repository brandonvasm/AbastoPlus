from dataclasses import dataclass, field
from typing import List
import uuid

from shared.domain.value_objects.customerid_value_object import CustomerId
from .order_status_value_object import OrderStatus
from .orderid_value_object import OrderItem


@dataclass
class Order:
    id: str
    customer_id: CustomerId
    status: OrderStatus
    items: List[OrderItem] = field(default_factory=list)

    @staticmethod
    def create(customer_id: CustomerId) -> "Order":
        return Order(
            id=str(uuid.uuid4()),
            customer_id=customer_id,
            status=OrderStatus.CONFIRMED,
            items=[]
        )