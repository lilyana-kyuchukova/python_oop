from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses(self):
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for pos in self.sponsors.values():  # [{1: 100000, 2: 50000}] iterates the 1st dict
            for p in pos.keys():  # [1, 2] iterates the keys
                if race_pos <= p:
                    revenue += pos[p]
                    break

        revenue -= self.expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
