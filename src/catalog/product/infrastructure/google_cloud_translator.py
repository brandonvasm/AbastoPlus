from catalog.product.application.ports.translate_service import TranslateService
from googletrans import Translator


class GoogleCloudTranslator(TranslateService):
    def __init__(self):
        pass
    
    def translate(self, text: str, target_language: str) -> str:
        self.client = Translator()
        result = self.client.translate(text, dest=target_language)
        return result.text
    