from NeedforSpeed.motorcycle import MotorCycle


class RaceMotorcycle(MotorCycle):
    DEFAULT_FUEL_CONSUMPTION: 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)