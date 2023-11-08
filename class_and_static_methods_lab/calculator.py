import functools
from typing import List


class Calculator:
    @staticmethod
    def add(*args: List[int]):
        # for consistency with reduce otherwise sum(args)
        return functools.reduce(lambda a, b: a + b, args)

    @staticmethod
    def multiply(*args: List[int]):
        return functools.reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args: List[int]):
        return functools.reduce(lambda a, b: a + b if a == 0 or b == 0 else a / b, args)

    @staticmethod
    def subtract(*args: List[int]):
        return functools.reduce(lambda a, b: a - b, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2, 0))
print(Calculator.subtract(90, 20, -50, 43, 7))
