from value_objects.product_base_unit import ProductBaseUnitValueObject
from value_objects.product_id import IdValueObject
from value_objects.product_name import ProductNameValueObject

class Product:
    def __init__(
        self,
        id: IdValueObject,
        name: ProductNameValueObject,
        baseUnit: ProductBaseUnitValueObject
    ):
        self.__productId = id
        self.__productName = name
        self.__productBaseUnit = baseUnit

    def build(
        id: str,
        name: str,
        baseUnit: str
    ):
        return Product(
            IdValueObject(id),
            ProductNameValueObject(name),
            ProductBaseUnitValueObject(baseUnit)
        ) 


