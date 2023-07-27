"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Happen when we enter non-integer value to numerator and denominator.
2. When will a ZeroDivisionError occur?
Happen when we enter zero to denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero.Please enter correct number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
