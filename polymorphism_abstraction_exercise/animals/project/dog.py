from project.animal import Animal


class Dog(Animal):

    @staticmethod
    def make_sound():
        return "Woof!"


dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)