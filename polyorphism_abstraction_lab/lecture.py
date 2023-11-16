from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("Method must be implemented in subclass")


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def perimeter(self):
        pass

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2



my_rectangle = Rectangle(2, 3)
my_circle = Circle(3)

print("Area on rectangle: ", my_rectangle.area())
print("Area on circle: ", my_circle.area())
print(my_rectangle.perimeter())


