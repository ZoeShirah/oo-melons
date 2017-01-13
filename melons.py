"""This file should have our order classes in it."""
from random import randint


class AbstractMelonOrder(object):
    """A basic melon order."""

    def __init__(self, species, qty, order_type=None, tax=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        """pick a random number between 5-9 as base price"""

        base_price = randint(5, 9)
        return base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international":
            if self.qty < 10:
                total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A US government melon order"""
    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
