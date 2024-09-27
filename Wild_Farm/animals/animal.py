from abc import ABC, abstractmethod

from Wild_Farm.food import Food


class Animal(ABC):
    POSSIBLE_FOODS = []
    INCREASED_WEIGHT = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.foot_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.POSSIBLE_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.INCREASED_WEIGHT
        self.foot_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.foot_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.foot_eaten}]"
