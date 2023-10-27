class Cup:
    def __init__(self, capacity: int, quantity: int):
        self.size = capacity
        self.quantity = quantity
        self.availability = capacity - quantity

    def fill(self, quantity) -> None:
        if self.availability >= quantity:
            self.quantity += quantity
            self.availability -= quantity

    def status(self) -> int:
        return self.availability


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
