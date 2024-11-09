from unittest import TestCase, main

from TennisPlayers.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.tennis_player = TennisPlayer('Ivan', 38, 100)

    def test_correct_initializing(self):
        self.assertEqual('Ivan', self.tennis_player.name)
        self.assertEqual(38, self.tennis_player.age)
        self.assertEqual(100, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_if_not_correct_name(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'Go'
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_if_age_is_not_correct_rise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_correct_add(self):
        self.tennis_player.add_new_win('Australia Open')
        self.assertEqual(self.tennis_player.wins, ['Australia Open'])

    def test_correct_lt(self):
        self.player = TennisPlayer('Meho', 30, 199)
        self.other = TennisPlayer('Pesho', 27, 200)
        result = self.player < self.other
        self.assertEqual(result, "Pesho is a top seeded player and he/she is better than Meho")

    def test_if_player_win(self):
        self.player = TennisPlayer('Meho', 30, 200)
        self.other = TennisPlayer('Pesho', 27, 199)
        result = self.player < self.other
        self.assertEqual(result, 'Meho is a better player than Pesho')

if __name__ == '__main__':
    main()
