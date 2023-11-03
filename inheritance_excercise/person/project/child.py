from project.person import Person


class Child(Person):
    # pass

    def __init__(self, name: str, age: int):
        super().__init__(name, age)