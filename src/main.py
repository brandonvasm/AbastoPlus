from catalog.product.infrastructure.product_container import ProductContainer 

import uuid


idd = str(uuid.uuid4())
print(idd)

container = ProductContainer()
saveproduct = container.save_product()

saveproduct.execute(
    {"id": idd, 
     "name": "Breakfast Burrito", 
     "unit_of_measure": "kg", 
     "presentations": 
        [
         {"id": str(uuid.uuid4()),
          "name": "Burrito de Desayuno Especial", 
          "net_quantity": 5,
          "type": "bag", 
          "unit_of_measure": "kg"}
        ]
    }
)
