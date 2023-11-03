from project.mammal import Mammal


class Gorilla(Mammal):
    # pass OR
    def __init__(self, name: str):
        super().__init__(name)
