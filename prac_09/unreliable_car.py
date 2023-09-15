from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """A version of Car with unreliable driving."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if the reliability check is passed."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
