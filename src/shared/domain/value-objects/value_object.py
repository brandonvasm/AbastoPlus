from typing import TypeVar, Generic

T = TypeVar('T')

class ValueObject:
    def __init__(self, value: T):
        self._value = value

    def toString(self) -> str:
        return str(self._value)
