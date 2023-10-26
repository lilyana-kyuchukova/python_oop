class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"This is class Person with instance {self.name}"


lilly = Person("Lilly", "F")

print(lilly.__dict__)
print(lilly)