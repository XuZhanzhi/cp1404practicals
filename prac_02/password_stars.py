MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Your password doesn't meet a minimum length set.")
        password = input("Please enter your password: ")
    return password


main()
