from .value_object import ValueObject
from enum import Enum

class EnumValueObject(ValueObject):
    def __init__(self, value: str):
        self._value = value
        self.__validValues: list[str] = [] 
        self._ensureValueIsValid(self._value)
    
    def _ensureValueIsValid(self, value: str):
        if not isinstance(value, str):
            raise Exception("El valor no es una cadena")
    
    def toString(self) -> str:
        return self._value

        