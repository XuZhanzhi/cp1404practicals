from prac_07.project import Project

FILENAME = "projects.txt"
MENU = "\
- (L)oad projects\n\
- (S)ave projects\n\
- (D)isplay projects\n\
- (F)ilter projects by date\n\
- (A)dd new project\n\
- (U)pdate project\n\
- (Q)uit"


def main():
    """Displaying the menu and get user's input."""
    projects = []
    print(MENU)
    user_input = input(">>>").upper()
    while user_input != "Q":
        if user_input == "L":
            load_file(projects)
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


def load_file(projects):
    """This function is for loading file"""
    file_name = input("File Name:\n>>>")
    try:
        infile = open(file_name, 'r')
    except FileNotFoundError:
        print(f"file not found, using the default file: {FILENAME}")
        file_name = FILENAME
        infile = open(file_name, 'r')
    infile.readline()
    for line in infile:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    infile.close()
    print(f"Data loaded from {file_name}")
