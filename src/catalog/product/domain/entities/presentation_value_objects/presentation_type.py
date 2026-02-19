from shared.domain.value_objects.enum_value_object import EnumValueObject

class PresentationType(EnumValueObject):
    def __init__(self, value):
        super().__init__(value)
        self.__validValues = ["bag", "sack", "box", "can", "jar", "bottle"]
        self._validateTypes(self._value)

    def _validateTypes(self, value):
        if value not in self.__validValues:
            raise Exception("El tipo no es valido")