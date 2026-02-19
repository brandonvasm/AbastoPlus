from shared.domain.value_objects.string_value_object import StringValueObject

class PresentationName(StringValueObject):
    def __init__(self, value):
        super().__init__(value)
