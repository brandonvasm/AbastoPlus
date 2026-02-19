from shared.domain.value_objects.int_value_object import IntValueObject

class PresentationNetQuantity(IntValueObject):
    def __init__(self, value):
        super().__init__(value)
