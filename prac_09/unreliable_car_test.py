from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create two cars with different reliabilities
    good_car = UnreliableCar("Good Car", 100, 90)
    bad_car = UnreliableCar("Bad Car", 100, 9)

    # drive the cars many times and print the distance driven
    for i in range(1, 11):
        print(f"Drive {i}km:")
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()
