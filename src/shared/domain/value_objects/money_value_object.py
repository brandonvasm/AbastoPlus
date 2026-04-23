class Money:
    amount: float
    currency: str

    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    @staticmethod
    def create(amount: float, currency: str) -> "Money":
        if amount < 0:
            raise InvalidMoneyError("Amount cannot be negative")

        if not currency or not isinstance(currency, str):
            raise InvalidMoneyError("Invalid currency")

        return Money(amount, currency)

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise CurrencyMismatchError("Currencies must match")

        return Money(self.amount + other.amount, self.currency)

    def equals(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False

        return (
            self.amount == other.amount and
            self.currency == other.currency
        )


class InvalidMoneyError(Exception):
    pass


class CurrencyMismatchError(Exception):
    pass