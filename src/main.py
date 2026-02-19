from catalog.product.domain.product import Product
from catalog.product.domain.presentation_primitive import PrimitivePresentation
import uuid

idd = str(uuid.uuid4())
print(idd)
product = Product.build(idd, "Carlos Eduardo Vela", "kg", 
            [
                PrimitivePresentation(
                    str(uuid.uuid4()),
                    "Presentacion1", 5, "bag", "kg"
                )
            ])
