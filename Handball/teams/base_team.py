from abc import ABC, abstractmethod


class BaseTeam(ABC):

    def __init__(self, name, country, advantage, budget):

        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Team name cannot be empty!')
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError('Team country should be at least 2 symbols long!')
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError('Advantage must be greater than zero!')
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistic(self):
        total_price = sum([x.price for x in self.equipment])
        average_protection = sum([x.protection for x in self.equipment]) / len(self.equipment) if self.equipment else 0
        result = [f"Name: {self.name}", f"Country: {self.country}", f"Advantage: {self.advantage} points",
                  f"Budget: {self.budget:.2f}EUR", f"Wins: {self.wins}",
                  f"Total Equipment Price: {total_price:.2f}", f"Average protection: {int(average_protection)}"]

        return '\n'.join(result)
