from unittest import TestCase, main

from testing.List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer = IntegerList('50', False, 1, 2.6, 2, 3)

    def test_correct_initializing(self):
        self.assertEqual([1, 2, 3], self.integer._IntegerList__data)

    def test_if_add_element_not_type_int(self):
        with self.assertRaises(ValueError) as ve:
            self.integer.add('50')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_correct_add_correct_type_number(self):
        self.integer.add(4)
        self.assertEqual([1, 2, 3, 4], self.integer._IntegerList__data)

    def test_not_correct_index_rise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer.remove_index(10)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_correct_index(self):
        self.integer.remove_index(1)
        self.assertNotIn(2, self.integer._IntegerList__data)

    def test_if_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer.get(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct_index(self):
        result = self.integer.get(1)
        self.assertIn(result, self.integer._IntegerList__data)

    def test_if_index_is_out_of_range_rise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer.insert(10, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_type_element_is_not_int_rise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.integer.insert(0, '5')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct(self):

        self.integer.insert(2, 4)

        self.assertEqual([1,2,4,3], self.integer._IntegerList__data)

    def test_correct_get_biggest_number(self):

        self.assertEqual(3, self.integer.get_biggest())

    def test_correct_get_index(self):

        self.assertEqual(2, self.integer.get_index(3))


if __name__ == '__main__':
    main()
