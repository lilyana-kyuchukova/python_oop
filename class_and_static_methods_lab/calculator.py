import functools


class Calculator:
    @staticmethod
    def add(*args):
        return functools.reduce(lambda a, b: a + b, args)
        # return sum(args)

    @staticmethod
    def multiply(*args):
        return functools.reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args):
        return functools.reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args):
        return functools.reduce(lambda a, b: a - b, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
