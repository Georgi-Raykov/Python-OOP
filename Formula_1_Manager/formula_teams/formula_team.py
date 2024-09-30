from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses(self):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos):
        value = 0
        for positions in self.sponsors.values():
            for pos in positions:
                if race_pos <= pos:
                    value += positions[pos]
                    break
        value -= self.expenses
        self.budget += value
        return f"The revenue after the race is {value}$. Current budget {self.budget}$"
