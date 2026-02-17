from shared.domain.value_objects.string_value_object import StringValueObject

class ProductNameValueObject(StringValueObject):
    def __init__(self, value):
        super().__init__(value)
        self._validateCharacterLength(self._value)

    def _validateCharacterLength(self, value):
        if not len(value) > 4:
            raise Exception("El nombre no tiene suficientes caracteres") 
        