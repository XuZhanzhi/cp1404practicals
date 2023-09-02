class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}," \
               f" completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """For sorting projects by priority"""
        return self.priority < other.priority

    def __eq__(self, other):
        """For checking if two projects have the same priority."""
        return self.priority == other.priority

    def is_complete(self):
        """For checking if the project is completed."""
        return self.completion_percentage == 100
