from value_object import ValueObject
import uuid

class IdentifierValueObject(ValueObject):
    def __init__(self, value: str):
        self._value = value
        self._ensureValueIsUuid(self._value)
    
    def _ensureValueIsUuid(self, value):
        try:
            uuid.UUID(value)
        except:
            raise Exception("El identificador no es valido.")

        if not isinstance(value, str):
            raise Exception("El valor no es una cadena")
        