from dependency_injector import containers, providers
from shared.infraestructure.order.in_memory_product_repository import InMemoryProductRepository
from shared.infraestructure.order.in_memory_order_repository import InMemoryOrderRepository
from shared.application.place_order_handler import PlaceOrderHandler

class OrderContainer(containers.DeclarativeContainer):
    product_repository = providers.Singleton(InMemoryProductRepository)
    order_repository = providers.Singleton(InMemoryOrderRepository)
    order_handler = providers.Factory(
        PlaceOrderHandler,
        order_repo=order_repository,
        product_repo=product_repository
    )
