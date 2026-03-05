from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class ValueObject:
    def __init__(self, value: T):
        self._value = value
    
    @abstractmethod
    def __str__(self) -> str:
        pass
