from .value_objects.product_base_unit import ProductBaseUnitValueObject
from .value_objects.product_id import IdValueObject
from .value_objects.product_name import ProductNameValueObject
from .presentation_primitive import PrimitivePresentation
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
        productPresentations: list[PrimitivePresentation] 
    ):
        return Product(
            IdValueObject(id),
            ProductNameValueObject(name),
            ProductBaseUnitValueObject(baseUnit),
            ProductPresentations(productPresentations, baseUnit)
        ) 


