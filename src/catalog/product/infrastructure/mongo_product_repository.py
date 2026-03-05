from catalog.product.application.product_repository import ProductRepository
from catalog.product.domain.product import Product
from pymongo import MongoClient

class MongoProductRepository(ProductRepository):
    def __init__(self):
        db = self.get_db()
        self.database = db["abasto_plus"] 
        self.collection = self.database["products"]

    def save(self, data: Product):
        product = data.toDict()
        self.collection.insert_one( 
            product
        )

    def get_db(self):
        client = MongoClient("mongodb://localhost:27017")
        db = client["abasto_plus"]
        return db

