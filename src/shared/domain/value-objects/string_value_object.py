from value_object import ValueObject

class StringValueObject(ValueObject):
    def __init__(self, value: str):
        self._value = value
        self._ensureValueIsString(self._value)
    
    def _ensureValueIsString(self, value):
        if not isinstance(value, str):
            raise Exception("El valor no es una cadena")
