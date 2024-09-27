from Wild_Farm.animals.animal import Mammal
from Wild_Farm.food import Food


class Mouse(Mammal):
    POSSIBLE_FOODS = ['Vegetable', 'Fruit']
    INCREASED_WEIGHT = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    POSSIBLE_FOODS = ['Meat']
    INCREASED_WEIGHT = 0.40

    def make_sound(self):
        return 'Woof'


class Cat(Mammal):
    POSSIBLE_FOODS = ['Meat', 'Vegetable']
    INCREASED_WEIGHT = 0.30

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    POSSIBLE_FOODS = ['Meat']
    INCREASED_WEIGHT = 1.00

    def make_sound(self):
        return 'ROAR!!!'
