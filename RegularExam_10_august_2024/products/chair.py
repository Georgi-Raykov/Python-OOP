from RegularExam_10_august_2024.products.base_product import BaseProduct


class Chair(BaseProduct):

    def __init__(self, model, price):
        super().__init__(model, price, 'Wood', 'Furniture')

    def discount(self):
        self.price -= self.price * 0.10
