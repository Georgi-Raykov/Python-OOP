class Flower:

    def __init__(self, name, water_requirements):

        self.name = name
        self.water_requirement = water_requirements
        self.is_happy = False

    def water(self, quantity):

        if quantity >= self.water_requirement:
            self.is_happy = True
        else:
            self.is_happy = False

    def status(self):

        return f"{self.name} {'is' if self.is_happy else 'is not'} happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
