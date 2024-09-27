from abc import ABC


class Food(ABC):

    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food, ABC):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food, ABC):

    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food, ABC):

    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food, ABC):

    def __init__(self, quantity):
        super().__init__(quantity)
