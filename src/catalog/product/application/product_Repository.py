from catalog.product.domain.product import Product
from abc import ABC, abstractmethod

class ProductRepository(Product):
    @abstractmethod
    def save(self, data: Product):
        pass 