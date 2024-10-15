from RegularExam_10_august_2024.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):

    def __init__(self, model, price):
        super().__init__(model, price, 'Wood/Plastic', 'Toys')

    def discount(self):
        self.price -= self.price * 0.20
