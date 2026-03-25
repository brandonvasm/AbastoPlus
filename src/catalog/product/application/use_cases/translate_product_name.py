from catalog.product.application.ports.translate_service import TranslateService
from catalog.product.application.product_repository import ProductRepository

class TranslateProductName:
    def __init__(self,
                 translate_service: TranslateService, 
                 product_repository: ProductRepository):
        self.translate_service = translate_service
        self.__product_repository = product_repository
        
    def execute(self, payload: dict):
        product_id = payload.get("product_id")
        product_name = payload.get("product_name")
        target_language = payload.get("target_language")

        translation = self.translate_service.translate(product_name, target_language)
        self.__product_repository.update(product_id, {"$set": {"name": translation}})
