class Quantity:
    def __init__(self, value: int):
        if value <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.value = value

    @staticmethod
    def create(value: int) -> "Quantity":
        return Quantity(value)

    def equals(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return False

        return self.value == other.value
    
    def __eq__(self, value):
        if not isinstance(value, Quantity):
            return False

        return self.equals(value)