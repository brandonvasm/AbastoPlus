from abc import ABC, abstractmethod
from shared.domain.value_objects.order import Order

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def find_by_id(self, order_id: str) -> Order:
        pass
    