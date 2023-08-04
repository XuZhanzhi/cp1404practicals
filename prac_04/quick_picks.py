import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_LINE = 6


def main():
    """This is the main function for picking numbers and print them"""
    num_quick_picks = int(input("How many quick picks do you want to generate? "))
    while num_quick_picks < 0:
        print("Please enter a correct number.")
        num_quick_picks = int(input("How many quick picks do you want to generate? "))
