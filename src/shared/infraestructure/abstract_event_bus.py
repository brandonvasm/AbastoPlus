from abc import ABC,abstractmethod


class AbstractEventBus(ABC):
    @abstractmethod
    def publish(self, event):
        pass
    
    @abstractmethod
    def consume(self, eventName:str, limit:int):
        pass