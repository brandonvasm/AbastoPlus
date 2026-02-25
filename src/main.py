from catalog.product.domain.product import Product
from catalog.product.domain.presentation_primitive import PrimitivePresentation
from catalog.product.infrastructure.MongoProductRepository import MongoProductRepository
import uuid

idd = str(uuid.uuid4())
print(idd)
product = Product.build(idd, "Carlos Eduardo Vela", "kg", 
            [
                PrimitivePresentation(
                    str(uuid.uuid4()),
                    "Presentacion2", 5, "bag", "kg"
                )
            ])
print(product.toDict())
prueva = MongoProductRepository()
prueva.save(product)
