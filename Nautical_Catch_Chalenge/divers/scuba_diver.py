from Nautical_Catch_Chalenge.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    MAXIMUM_OXYGEN = 540

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.MAXIMUM_OXYGEN)

    def miss(self, time_to_catch):

        value = round(time_to_catch * 0.30)
        if self.oxygen_level < value:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= value

    def renew_oxy(self):

        self.oxygen_level = self.MAXIMUM_OXYGEN


