from prac_07.project import Project
import datetime

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
            filter_projects(projects)
        elif user_input == "A":
            add_project(projects)
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


def filter_projects(projects):
    """This function is for filtering projects by date"""
    is_completed = False
    while not is_completed:
        try:
            filter_date_string = input("Show Projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
            is_completed = True
        except ValueError:
            print("Invalid date try again")
    for project in projects:
        date_string = project.start_date
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        if date >= filter_date:
            print(project)


def add_project(projects):
    """This function is for adding a new project."""
    print("Let's add a new project")
    # get name
    name = input("Name: ")
    is_finished = True
    while is_finished:
        # get start date
        try:
            date_string = input("Start date (dd/mm/yy): ")
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_finished = False
        except ValueError:
            print("Invalid Start date (dd/mm/yyyy)")
    while not is_finished:
        # get priority
        try:
            priority = int(input("Priority: "))
            is_finished = True
        except ValueError:
            print("Invalid priority please enter a priority number")
    while is_finished:
        # get cost
        try:
            cost_estimate = float(input("Cost Estimate: $"))
            is_finished = False
        except ValueError:
            print("Invalid cost, please enter valid cost number")
    while not is_finished:
        # get completion percentage
        try:
            completion_percentage = int(input("Percent Compete: "))
            if completion_percentage > 100:
                print("invalid percentage")
            else:
                is_finished = True
        except ValueError:
            print("Invalid percentage, please enter valid percentage")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


main()
