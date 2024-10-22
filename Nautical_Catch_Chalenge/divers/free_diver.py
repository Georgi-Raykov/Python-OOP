from Nautical_Catch_Chalenge.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    MAXIMUM_OXYGEN = 120

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.MAXIMUM_OXYGEN)

    def miss(self, time_to_catch):

        value = round(time_to_catch * 0.60)
        if self.oxygen_level < value:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= value

    def renew_oxy(self):
        self.oxygen_level = self.MAXIMUM_OXYGEN




