from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerId:
    value: str

    @staticmethod
    def from_value(value: str) -> "CustomerId":
        if not value or not value.strip():
            raise ValueError("CustomerId cannot be empty")

        return CustomerId(value)