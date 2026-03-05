from catalog.product.domain.product import Product
from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def save(self, data: Product):
        pass