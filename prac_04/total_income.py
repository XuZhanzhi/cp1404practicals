"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_number = int(input("How many months? "))

    for month in range(1, months_number + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income(incomes)


def print_income(incomes):
    """This function is used for printing income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
