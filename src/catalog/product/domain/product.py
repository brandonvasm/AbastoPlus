from .value_objects.product_base_unit import ProductBaseUnitValueObject
from .value_objects.product_id import IdValueObject
from .value_objects.product_name import ProductNameValueObject
from .value_objects.product_presentations import ProductPresentations

class Product:
    def __init__(
        self,
        id: IdValueObject,
        name: ProductNameValueObject,
        baseUnit: ProductBaseUnitValueObject,
        productPresentations: ProductPresentations
    ):
        self.__productId = id
        self.__productName = name
        self.__productBaseUnit = baseUnit
        self.__productPresentations = productPresentations

    def build(
        id: str,
        name: str,
        baseUnit: str,
        productPresentations: list[dict] 
    ):
        return Product(
            IdValueObject(id),
            ProductNameValueObject(name),
            ProductBaseUnitValueObject(baseUnit),
            ProductPresentations(productPresentations, baseUnit)
        ) 
    
    def toDict(self):
        return {
            "_id": str(self.__productId),
            "name": str(self.__productName),
            "base_unit": str(self.__productBaseUnit),
            "presentations": self.__productPresentations.convertToDict()
        }


