from catalog.product.domain.product import Product
from catalog.product.application.product_repository import ProductRepository
from catalog.product.application.ports.translate_service import TranslateService
from shared.domain.abstract_event_bus import AbstractEventBus

class SaveProduct:
    def __init__(self, 
                 repository: ProductRepository, 
                 translator: TranslateService, 
                 event_bus: AbstractEventBus):
        self.__repository = repository
        self.__translator = translator
        self.__event_bus = event_bus

    def execute(self, data: dict):
        primitive_presentations = data["presentations"]
        presentations = []

        for presentation in primitive_presentations:
            translation = self.__translator.translate(presentation["name"], "en")
            presentation["name"] = translation
            presentations.append(presentation)


        self.__repository.save( 
            data = Product.build(
                data["id"],
                data["name"],
                data["unit_of_measure"],
                presentations
            )
        )

        self.__event_bus.publish({
            "name": "catalog.product.created_event",
            "payload": {
                "product_id": data["id"],
                "product_name": data["name"],
                "target_language": "en"
            }
        })
