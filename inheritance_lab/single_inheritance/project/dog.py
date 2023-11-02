from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."


dog = Dog()
cat = Animal()
print(dog.eat())
print(dog.bark())
print(cat.eat())  # cat is Animal and can only eat, cannot bark
