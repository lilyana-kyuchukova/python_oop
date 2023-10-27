#  some custom way to initiate without __init__
class Example:
    def __new__(cls, name, age):
        obj = super().__new__()
        obj.attr1 = name
        obj.attr2 = age

        return obj


class Point:
    def __init__(self, x, y):
        self.x = list()
        self.y = list()

    def __eq__(self, other):  # compares 2 instances
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, item):
        return self.y[item]

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(len(p1))
print(p1[0])
p3 = p1 + p2
print(p3.x, p3.y)
