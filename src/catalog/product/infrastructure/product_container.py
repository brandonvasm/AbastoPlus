from dependency_injector import containers, providers
from catalog.product.application.use_cases.save_product import SaveProduct
from catalog.product.application.use_cases.translate_presentation_name import TranslatePresentationName
from catalog.product.application.use_cases.translate_product_name import TranslateProductName
from catalog.product.infrastructure.mongo_product_repository import MongoProductRepository
from catalog.product.infrastructure.google_cloud_translator import GoogleCloudTranslator
from shared.infraestructure.event_bus import EventBus

class ProductContainer(containers.DeclarativeContainer):
    repository = providers.Singleton(MongoProductRepository)
    translator = providers.Singleton(GoogleCloudTranslator)
    event_bus = providers.Singleton(EventBus)
    translate_presentation_name = providers.Factory(
        TranslatePresentationName, 
        translate_service=translator
    )
    translate_product_name = providers.Factory(
        TranslateProductName, 
        translate_service=translator, 
        product_repository=repository
    )   
    save_product = providers.Factory(SaveProduct, repository=repository, translator=translator, event_bus=event_bus)
