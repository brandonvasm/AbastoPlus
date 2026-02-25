from ..entities.presentation import Presentation
from ..presentation_primitive import PrimitivePresentation

class ProductPresentations:
    def __init__(
        self,
        presentations: list[PrimitivePresentation],
        productBaseUnit: str
    ):
        self.__productPresentations: list[Presentation] = [] 
        for presentation in presentations:

            if not presentation.unit_of_measure == productBaseUnit:
                raise Exception("The measure unit of the presentation is not valid")

            self.__productPresentations.append(
                Presentation.build(
                    presentation.id,
                    presentation.name,
                    presentation.netQuantity,
                    presentation.type,
                    presentation.unit_of_measure
                )
            )

    def convertToDict(self):
        presentations = []
        for presentation in self.__productPresentations:
            presentations.append(
                presentation.toDict()
            )
        return presentations