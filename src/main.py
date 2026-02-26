from catalog.product.domain.product import Product
from catalog.product.domain.presentation_primitive import PrimitivePresentation
from catalog.product.infrastructure.MongoProductRepository import MongoProductRepository
from catalog.product.application.use_cases.save_product import SaveProduct
import uuid


idd = str(uuid.uuid4())
print(idd)

mongo = MongoProductRepository()
saveproduct = SaveProduct(mongo)


saveproduct.execute({"id": idd, "name": "Breakfast Burrito", "unit_of_measure": "kg", "presentations": [{"id": str(uuid.uuid4()),"name": "Presentacion 2", "net_quantity": 5,"type": "bag", "unit_of_measure": "kg"}]})








