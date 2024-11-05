from Booth.booths.open_booth import OpenBooth
from Booth.booths.private_booth import PrivateBooth
from Booth.delicacies.gingerbread import Gingerbread
from Booth.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):

        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price):

        valid_delicacy = {'Gingerbread': Gingerbread, 'Stolen': Stolen}

        for delicacy in self.delicacies:

            if delicacy.name == name:
                raise Exception(f"{name} already exist!")

        if type_delicacy not in valid_delicacy:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        delicacy = valid_delicacy[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):

        valid_booth = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exist!")

        if type_booth not in valid_booth:
            raise Exception(f"{type_booth} is a not valid booth!")
        booth = valid_booth[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):

        booth = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people][0]

        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):

        booth = self.__find_booth_by_number(booth_number)
        delicacy = self.__find_delicacy_by_name(delicacy_name)

        if booth is None:
            raise Exception(f'Could not find booth {booth_number}')
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_order.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):

        booth = self.__find_booth_by_number(booth_number)
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_order)
        self.income += bill
        booth.delicacy_order = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\n"\
               f"Bill: {bill:.2f}lv."

    def get_income(self):

        return f"Income: {self.income:.2f}lv."

    def __find_booth_by_number(self, number):

        for booth in self.booths:
            if booth.booth_number == number:
                return booth
        return None

    def __find_delicacy_by_name(self, name):

        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy
        return None
