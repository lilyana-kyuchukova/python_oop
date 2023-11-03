from project.reptile import Reptile


class Snake(Reptile):
    # pass OR
    def __init__(self, name: str):
        super().__init__(name)