from shared.domain.value_objects.enum_value_object import EnumValueObject

class PresentationMeasureUnits(EnumValueObject):
    def __init__(self, value):
        super().__init__(value)
        self.__validValues = ["kg", "g", "oz", "lb", "ml", "lt", "unit"]
        self._validateBaseUnits(self._value)
    
    def _validateBaseUnits(self, value):
        if value not in self.__validValues:
            raise Exception("Algunos valores no tienen unidades validas")
            