def main():
    """This is the main function for getting email and print email with names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        prefix = email.split('@')[0]
        parts = prefix.split('.')
        name = " ".join(parts).title()
        confirmation = input(f"Is your name {name}? (Y/n)")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
