import pytest
from shared.domain.value_objects.money_value_object import Money, InvalidMoneyError, CurrencyMismatchError


class TestCreate:

    def test_creates_money_with_valid_amount(self):
        money = Money.create(10.50, "USD")
        
        assert money.amount == 10.50
        assert money.currency == "USD"

    def test_throws_for_negative_amount(self):
        with pytest.raises(InvalidMoneyError):
            Money.create(-1, "USD")


class TestAdd:

    def test_adds_two_money_values_with_same_currency(self):
        a = Money.create(10, "USD")
        b = Money.create(20, "USD")

        result = a.add(b)

        assert result.amount == 30
        assert result.currency == "USD"

    def test_throws_for_different_currencies(self):
        usd = Money.create(10, "USD")
        eur = Money.create(10, "EUR")

        with pytest.raises(CurrencyMismatchError):
            usd.add(eur)


class TestEquality:

    def test_equals_money_with_same_amount_and_currency(self):
        a = Money.create(10, "USD")
        b = Money.create(10, "USD")

        assert a.equals(b) is True

    def test_not_equal_with_different_amount(self):
        a = Money.create(10, "USD")
        b = Money.create(20, "USD")

        assert a.equals(b) is False

