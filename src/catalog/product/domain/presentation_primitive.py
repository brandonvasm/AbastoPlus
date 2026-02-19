class PrimitivePresentation:
    def __init__(
        self,
        id: str,
        name: str,
        net_quantity: int,
        type: str,
        unit_of_measure: str 
    ):
        self.id: str = id
        self.name: str = name
        self.netQuantity: int = net_quantity
        self.type: str = type
        self.unit_of_measure: str = unit_of_measure
