class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """a programming language has a name,typing,reflection and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """determine the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """return the string representation for the programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

