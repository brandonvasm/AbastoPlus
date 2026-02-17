from shared.domain.value_objects.enum_value_object import EnumValueObject

class ProductBaseUnitValueObject(EnumValueObject):
    def __init__(self, value):
        super().__init__(value)
    
    def _validateBaseUnits(self, value):
        values = ["kg", "g", "oz"]
        for value in self.__validValues:
            if value not in values:
                raise Exception("Algunos valores no tiene unidades validas")
            