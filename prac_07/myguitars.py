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


guitars = []

with open("guitars.csv") as file:
    for line in file:
        name, year, cost = line.strip().split(",")
        guitars.append(Guitar(name, int(year), float(cost)))

sorted_guitars = sorted(guitars, key=lambda x: x.year)

for guitar in sorted_guitars:
    print(guitar)
