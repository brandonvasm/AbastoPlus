from shared.domain.value_objects.identifier_value_object import IdentifierValueObject

class PresentationId(IdentifierValueObject):
    def __init__(self, value):
        super().__init__(value)