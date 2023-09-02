CURRENT_YEAR = 2023
VINTAGE = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not"""
        return self.get_age() >= VINTAGE
