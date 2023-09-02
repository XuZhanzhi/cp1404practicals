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
            save_file(projects)
        elif user_input == "D":
            display_projects(projects)
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
    """This function is for loading file."""
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


def save_file(projects):
    """This function is for saving projects to the file."""
    file_name = input("File Name:\n>>>")
    outfile = open(file_name, 'w')
    print(f"Name\tStart Data\tPriority\t"
          f"Cost Estimate\tCompletion Percentage", file=outfile)
    for project in projects:
        print(f"{project.name}\t{project.start_data}\t{project.priority}\t"
              f"{project.cost_estimate}\t{project.completion_percentage}", file=outfile)
    outfile.close()
    print(f"Data saved to {file_name}")


def display_projects(projects):
    """This function is for displaying two groups projects:incomplete projects and completed projects."""
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    complete_projects.sort()
    incomplete_projects.sort()
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)
    print("Compete Projects:")
    for project in complete_projects:
        print(project)


main()
