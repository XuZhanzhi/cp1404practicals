"""question 1"""
out_file = open("name.txt", "w")
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

"""question 2"""
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}.")

"""question 3"""
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
number_add = number1 + number2
print(number_add)

"""question 4"""
in_file = open("numbers.txt", "r")
total_number = 0
for line in in_file:
    number = int(line)
    total_number += number
in_file.close()
print(total_number)
