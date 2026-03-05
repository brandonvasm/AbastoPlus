from catalog.product.domain.product import Product


class SaveProduct:
    def __init__(self, repository, translator):
        self.__repository = repository
        self.__translator = translator

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
