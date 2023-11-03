from project.animal import Animal


class Reptile(Animal):
    # pass OR
    def __init__(self, name: str):
        super().__init__(name)
