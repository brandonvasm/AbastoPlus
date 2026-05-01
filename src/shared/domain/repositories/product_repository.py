from abc import ABC, abstractmethod
from shared.domain.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def find_by_id(self, product_id: str) -> Product:
        pass