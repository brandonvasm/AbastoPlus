from abc import ABC, abstractmethod

class TranslateService(ABC):
    @abstractmethod
    def translate(self, text: str, target_language: str) -> str:
        pass
    