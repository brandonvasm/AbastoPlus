from .value_object import ValueObject

class IntValueObject(ValueObject):
    def __init__(self, value: int):
        self._value = value
        self._ensureValueIsInt(self._value)
    
    def _ensureValueIsInt(self, value):
        if not isinstance(value, int):
            raise Exception("El valor no es un entero")
        