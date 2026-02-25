from .presentation_value_objects.presentation_id import PresentationId
from .presentation_value_objects.presentation_name import PresentationName
from .presentation_value_objects.presentation_net_quantity import PresentationNetQuantity
from .presentation_value_objects.presentation_type import PresentationType
from .presentation_value_objects.presentation_unit_of_measure import PresentationMeasureUnits

class Presentation:
    def __init__(
         self,
         id: PresentationId,
         name: PresentationName,
         net_quantity: PresentationNetQuantity,
         type: PresentationType,
         unit_of_measure: PresentationMeasureUnits
    ):
        self.__id = id
        self.__name = name
        self.__netQuantity = net_quantity
        self.__type = type
        self.__unitOfMeasure = unit_of_measure

    def build(
        id: str,
        name: str,
        net_quantity: int,
        type: str,
        unit_of_measure: str        
    ):
        return Presentation(
            PresentationId(id), 
            PresentationName(name), 
            PresentationNetQuantity(net_quantity),
            PresentationType(type), 
            PresentationMeasureUnits(unit_of_measure)
        )
    
    def toDict(self):
        return {
            "id": self.__id._value,
            "name": self.__name._value,
            "quantity": self.__netQuantity._value,
            "type": self.__type._value,
            "unit_of_measure": self.__unitOfMeasure._value
        }
    