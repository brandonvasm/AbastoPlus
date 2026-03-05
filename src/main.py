from catalog.product.infrastructure.container import Container

import uuid


idd = str(uuid.uuid4())
print(idd)

container = Container()
saveproduct = container.save_product()

saveproduct.execute(
    {"id": idd, 
     "name": "Breakfast Burrito", 
     "unit_of_measure": "kg", 
     "presentations": 
        [
         {"id": str(uuid.uuid4()),
          "name": "Presentacion 2", 
          "net_quantity": 5,
          "type": "bag", 
          "unit_of_measure": "kg"}
        ]
    }
)
