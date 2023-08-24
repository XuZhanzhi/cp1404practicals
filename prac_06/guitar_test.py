from prac_06.guitar import Guitar

CURRENT_YEAR = 2023


def run_test():
    """Test the last two methods work as expected."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    guitar_2 = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected {11}. Got {guitar_2.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected {False}. Got {guitar_2.is_vintage()}")


if __name__ == '__main__':
    run_test()
