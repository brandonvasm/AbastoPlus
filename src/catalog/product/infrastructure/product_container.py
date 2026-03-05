from dependency_injector import containers, providers
from catalog.product.application.use_cases.save_product import SaveProduct
from catalog.product.application.use_cases.translate_presentation_name import TranslatePresentationName
from catalog.product.infrastructure.mongo_product_repository import MongoProductRepository
from catalog.product.infrastructure.google_cloud_translator import GoogleCloudTranslator

class ProductContainer(containers.DeclarativeContainer):
    repository = providers.Singleton(MongoProductRepository)
    translator = providers.Singleton(GoogleCloudTranslator)
    translate_presentation_name = providers.Factory(
        TranslatePresentationName, 
        translate_service=translator
    )
    save_product = providers.Factory(SaveProduct, repository=repository, translator=translator)
