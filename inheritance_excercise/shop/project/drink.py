from project.product import Product


class Drink(Product):
    # QUANTITY = 10
    #
    # def __init__(self, name: str):
    #     super().__init__(name, Food.QUANTITY)
    def __init__(self, name: str):
        super().__init__(name, 10)
