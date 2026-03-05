from dependency_injector import containers, providers
from catalog.product.application.use_cases.save_product import SaveProduct
from catalog.product.infrastructure.MongoProductRepository import MongoProductRepository

class ProductContainer(containers.DeclarativeContainer):
    repository = providers.Singleton(MongoProductRepository)
    save_product = providers.Factory(SaveProduct, repository=repository)
