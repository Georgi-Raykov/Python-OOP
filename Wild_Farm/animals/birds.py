from Wild_Farm.animals.animal import Bird


class Owl(Bird):
    POSSIBLE_FOODS = ['Meat']
    INCREASED_WEIGHT = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    POSSIBLE_FOODS = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    INCREASED_WEIGHT = 0.35

    def make_sound(self):
        return "Cluck"
