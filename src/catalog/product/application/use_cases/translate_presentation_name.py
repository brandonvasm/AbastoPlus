from catalog.product.application.ports.translate_service import TranslateService

class TranslatePresentationName:
    def __init__(self, translate_service: TranslateService):
        self.translate_service = translate_service

    def execute(self, presentation_name: str, target_language: str) -> str:
        return self.translate_service.translate(presentation_name, target_language)