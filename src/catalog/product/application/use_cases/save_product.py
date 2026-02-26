from catalog.product.application.product_Repository import ProductRepository
from catalog.product.domain.presentation_primitive import PrimitivePresentation
from catalog.product.domain.product import Product
from typing import Type



class SaveProduct:
    def __init__(self, repository: Type[ProductRepository]):
        self.__repository = repository
        
        


    def execute(self, data: dict):
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
            data = Product.build(
                data["id"],
                data["name"],
                data["unit_of_measure"],
                presentations




            )
        )







    













    