from unittest import TestCase, main

from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):

        self.vehicle = Vehicle(50, 120)

    def test_correct_initializing(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(120, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_not_enough_fuel_rise_exception(self):

        with self.assertRaises(Exception) as ex:

            self.vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_fuel_is_enough(self):

        self.vehicle.drive(20)
        self.assertEqual(25, self.vehicle.fuel)

    def test_if_fuel_is_more_than_capacity_rise_Exception(self):

        with self.assertRaises(Exception) as ex:

            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_fuel_capacity(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(25)
        self.assertEqual(50, self.vehicle.fuel)
    def test_correct_str(self):

        self.assertEqual("The vehicle has 120 horse power with 50 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())
