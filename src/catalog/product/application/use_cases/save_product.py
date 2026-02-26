from product_Repository import ProductRepository
from domain.presentation_primitive import PrimitivePresentation
from catalog.product.domain.product import Product



class SaveProduct:
    def __init__(self, repository: ProductRepository):
        self.__repository = repository
        
        


    def Execute(self, data: dict):
        primitive_presentations = data["presentations"]
        presentations = []
        for p in primitive_presentations:
            presentations.append(
                PrimitivePresentation(
                    p["id"],
                    p["name"],
                    p["net_quantity"],
                    p["type"],
                    p["unit_of_measure"]
                )
            )

        self.__repository.save(
            Product.build(
                data["id"],
                data["name"],
                data["unit_of_measure"],
                presentations




            )
        )







    













    