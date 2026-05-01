from typing import List
import uuid

from shared.domain.value_objects.customerid_value_object import CustomerId
from shared.domain.value_objects.money_value_object import Money
from .order_status_value_object import OrderStatus
from .orderid_value_object import OrderItem
from .quantity_value_object import Quantity

class Order:
    id: str
    customer_id: CustomerId
    status: OrderStatus
    items: List[OrderItem] = []

    def __init__(self, id: str, customer_id: CustomerId, status: OrderStatus, items: List[OrderItem] | None = []):
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.items = items

    @staticmethod
    def create(
               customer_id: CustomerId, 
               status: OrderStatus = OrderStatus.DRAFT,
               items: List[OrderItem] | None = None
               ) -> "Order":
        return Order(
            id=str(uuid.uuid4()),
            customer_id=customer_id,
            status=status,
            items=items if items is not None else []
        )
    
    def add_item(self, product_id: str, quantity: int, unit_price: float, currency: str):        
        if self.status == OrderStatus.CANCELLED:
            raise ValueError("Cannot add items to a cancelled order")
        
        if product_id in [item.product_id for item in self.items]:
            existing_item = next(item for item in self.items if item.product_id == product_id)
            total_quantity = existing_item.quantity.value + quantity
            existing_item.quantity = Quantity.create(total_quantity)
            return
        
        self.items.append(OrderItem(product_id=product_id, 
                                    quantity=Quantity.create(quantity), 
                                    unit_price=Money(unit_price, currency)))