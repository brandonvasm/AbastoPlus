class TranslateProductName:
    def __init__(self, translate_service, product_repository):
        self.translate_service = translate_service
        self.__product_repository = product_repository
        
    def execute(self, **kwargs):
        product_id = kwargs.get("product_id")
        product_name = kwargs.get("product_name")
        target_language = kwargs.get("target_language")

        translation = self.translate_service(product_name, target_language)
        self.__product_repository.update(product_id, {"name": translation})
