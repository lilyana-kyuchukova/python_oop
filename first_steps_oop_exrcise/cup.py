class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.availability = size - quantity

    def fill(self, quantity):
        if self.availability >= quantity:
            self.quantity += quantity
            self.availability -= quantity

    def status(self):
        return self.availability


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())