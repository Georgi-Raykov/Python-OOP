from unittest import TestCase, main

from testing.CarManager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Opel', 'Vectra', 100, 60)

    def test_correct_initializing(self):
        self.assertEqual('Opel', self.car.make)
        self.assertEqual('Vectra', self.car.model)
        self.assertEqual(100, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_make_is_empty_and_return_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_model_is_empty_and_return_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_fuel_consumption_is_zero_rise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_capacity_less_than_zero_rise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_is_negative_rise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_number(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_is_more_fuel_capacity(self):
        self.car.refuel(self.car.fuel_capacity + 20)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_not_enough_fuel_rise_exception(self):

        self.car.fuel_amount = 50

        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


    def test_fuel_amount_is_enough_for_distance(self):
        self.car.fuel_amount = 100
        self.car.drive(90)
        self.assertEqual(self.car.fuel_amount, 10)

if __name__ == '__main__':
    main()
