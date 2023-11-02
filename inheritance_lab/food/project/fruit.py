from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str) -> None:
        super().__init__(expiration_date)
        self.name = name

    def get_info(self):
        return f"{self.name} with exp date {self.expiration_date}"


apple = Fruit("apple", "20/12/2023")
print(apple.get_info())
