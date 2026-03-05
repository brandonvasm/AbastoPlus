from ..entities.presentation import Presentation

class ProductPresentations:
    def __init__(
        self,
        presentations: list[dict],
        productBaseUnit: str
    ):
        self.__productPresentations: list[Presentation] = [] 

        for presentation in presentations:
            if not presentation["unit_of_measure"] == productBaseUnit:
                raise Exception("The measure unit of the presentation is not valid")

            self.__productPresentations.append(
                Presentation.build(
                    presentation["id"],
                    presentation["name"],
                    presentation["net_quantity"],
                    presentation["type"],
                    presentation["unit_of_measure"]
                )
            )

    def convertToDict(self):
        presentations = []
        for presentation in self.__productPresentations:
            presentations.append(
                presentation.toDict()
            )
        return presentations