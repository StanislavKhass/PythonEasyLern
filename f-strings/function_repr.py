#https://docs.python.org/3/library/string.html#formatspec
#here we are use modificator for f-string
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User's name is: {self.first_name} {self.last_name}"

user = User("John", "Doe")
print(f"{user}")
# John Doe
print(f"{user!r}")
# User's name is: John Doe
