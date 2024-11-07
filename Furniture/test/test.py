from unittest import TestCase, main

from Furniture.furniture import Furniture


class TestFurniture(TestCase):

    def setUp(self):
        self.furniture = Furniture('chair', 100, (10, 50, 40))

    def test_correct_initializing(self):
        self.assertEqual('chair', self.furniture.model)
        self.assertEqual(100, self.furniture.price)
        self.assertEqual((10, 50, 40), self.furniture.dimensions)
        self.assertEqual(True, self.furniture.in_stock)
        self.assertEqual(None, self.furniture.weight)

    def test_if_model_value_is_empty_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = '   '
        self.assertEqual("Model must be a non-empty string with a maximum length "
                         "of 50 characters.", str(ve.exception))

    def test_if_model_value_is_bigger_than_50_characters_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = 'vcvcvcvcxvxcvxcvxcvxcvxvxcvxcvxcvxcvvxvxvxcvxcvxvxcvxcvcxvxvvxcvxcvxcvxcvxcvxcvxcvxvxcvxcv'

        self.assertEqual("Model must be a non-empty string with a maximum length "
                         "of 50 characters.", str(ve.exception))

    def test_correct_price_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.price = -1

        self.assertEqual("Price must be a non-negative number.", str(ve.exception))

    def test_if_dimensions_len_is_more_less_three_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (10, 50, 40, 60)

        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ve.exception))

    def test_for_correct_values_in_dimensions_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (10, 50, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ve.exception))

    def test_for_correct_weight_value_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = 0

        self.assertEqual("Weight must be greater than zero.", str(ve.exception))

    def test_get_available_status(self):
        self.assertEqual("Model: chair is currently in stock.", self.furniture.get_available_status())

    def test_get_specification(self):
        self.assertEqual("Model: chair has the following dimensions: "
                         "10mm x 50mm x 40mm and weighs: N/A", self.furniture.get_specifications())


if __name__ == '__main__':
    main()


