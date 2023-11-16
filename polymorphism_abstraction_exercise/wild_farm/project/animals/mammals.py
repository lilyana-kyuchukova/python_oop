from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def gained_weight(self):
        return 0.10

    def food_eaten_by_type(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof"

    @property
    def gained_weight(self):
        return 0.40

    def food_eaten_by_type(self):
        return [Meat]


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def gained_weight(self):
        return 0.30

    def food_eaten_by_type(self):
        return [Vegetable, Meat]


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1.00

    def food_eaten_by_type(self):
        return [Meat]
