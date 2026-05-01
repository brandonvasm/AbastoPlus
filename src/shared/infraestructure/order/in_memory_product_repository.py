from shared.domain.repositories.product_repository import ProductRepository

class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.id] = product

    def find_by_id(self, product_id):
        return self.products.get(product_id)