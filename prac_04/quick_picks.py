import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_LINE = 6


def main():
    """This is the main function for picking numbers and print them"""
    num_quick_picks = int(input("How many quick picks do you want? "))
    while num_quick_picks < 0:
        print("Please enter a correct number.")
        num_quick_picks = int(input("How many quick picks do you want? "))

    for i in range(num_quick_picks):
        quick_pick_number = []
        for j in range(NUMBER_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick_number:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick_number.append(number)
        quick_pick_number.sort()
        print(" ".join(f"{number:2}" for number in quick_pick_number))


main()
