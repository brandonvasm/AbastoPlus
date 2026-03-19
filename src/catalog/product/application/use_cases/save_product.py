from catalog.product.domain.product import Product
from catalog.product.infrastructure.product_container import ProductContainer

class SaveProduct:
    def __init__(self, repository, translator):
        self.__repository = repository
        self.__translator = translator

    def execute(self, data: dict, event_bus):
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

        event_bus.publish({
            "name": "catalog.product.created_event",
            "payload": {
                "id": data["id"],
                "name": data["name"]
            }
        })
