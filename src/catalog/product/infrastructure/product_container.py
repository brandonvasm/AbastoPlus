from dependency_injector import containers, providers
from catalog.product.application.use_cases.save_product import SaveProduct
from catalog.product.application.use_cases.translate_presentation_name import TranslatePresentationName
from catalog.product.application.use_cases.translate_product_name import TranslateProductName
from catalog.product.infrastructure.mongo_product_repository import MongoProductRepository
from catalog.product.infrastructure.google_cloud_translator import GoogleCloudTranslator
from shared.infraestructure.in_memory_event_bus import InMemoryEventBus

class ProductContainer(containers.DeclarativeContainer):
    repository = providers.Singleton(MongoProductRepository)
    translator = providers.Singleton(GoogleCloudTranslator)
    translate_presentation_name = providers.Factory(
        TranslatePresentationName, 
        translate_service=translator
    )
    translate_product_name = providers.Factory(
        TranslateProductName, 
        translate_service=translator, 
        product_repository=repository
    )   
    event_bus = providers.Singleton(
        InMemoryEventBus,
        event_map=providers.Dict(
            {
            "catalog.product.created_event": [
                translate_product_name(),
            ],
            }
        )
        )
    save_product = providers.Factory(SaveProduct, repository=repository, translator=translator, event_bus=event_bus)
