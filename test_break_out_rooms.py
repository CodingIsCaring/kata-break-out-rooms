from unittest import TestCase
from break_out_rooms import break_out_rooms


class Test(TestCase):
    def test_one_round(self):
        self.assertEqual([["Yodra, Maria"]], break_out_rooms(1, ["Yodra", "Maria"], 2))

    def test_one_round_two_rooms(self):
        self.assertEqual([["Yodra, Maria", "Ana, Monica"]], break_out_rooms(1, ["Yodra", "Maria", "Ana", "Monica"], 2))

    def test_one_round_three_rooms(self):
        self.assertEqual([["Yodra, Maria", "Ana, Monica", "Lucia, Sara"]], break_out_rooms(1, ["Yodra", "Maria",
                                                                                               "Ana", "Monica",
                                                                                               "Lucia", "Sara"], 2))
