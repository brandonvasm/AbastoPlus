from abc import ABC, abstractmethod

class Event(ABC):
    @abstractmethod
    def __init__(self, name: str, payload: dict):
        pass

    def __str__(self):
        pass