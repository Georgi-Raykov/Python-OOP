from Booth.booths.booth import Booth


class OpenBooth(Booth):

    def __init__(self, booth_number, capacity):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people):
        price = number_of_people * 2.50
        self.price_for_reservation = price
        self.is_reserved = True
