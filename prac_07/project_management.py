from prac_07.project import Project

FILENAME = "projects.txt"
MENU: str = """(L)oad projects 
(S)ave Projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""


def main():
    """Displaying the menu and get user's input."""
    projects = []
    print(MENU)
    user_input = input(">>>").upper()
    while user_input != "Q":
        if user_input == "L":
            print()
        elif user_input == "S":
            print()
        elif user_input == "D":
            print()
        elif user_input == "F":
            print()
        elif user_input == "A":
            print()
        elif user_input == "U":
            print()
        else:
            print("Invalid Menu Choice")
        print(MENU)
        user_input = input(">>>").upper()
    print("Thank you for using custom-built project management software.")
