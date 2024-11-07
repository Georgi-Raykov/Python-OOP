from unittest import TestCase, main

from Mammal_Skeleton.mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Kety', 'Cat', 'meow')

    def test_correct_initializing(self):

        self.assertEqual('Kety', self.mammal.name)
        self.assertEqual('Cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_correct_sound(self):

        self.assertEqual("Kety makes meow",self.mammal.make_sound())

    def test_check_correct_get_kingdom(self):

        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_check_correct_info(self):

        self.assertEqual("Kety is of type Cat", self.mammal.info())


if __name__ == '_main_':
    main()

