from unittest import TestCase
from break_out_rooms import sum


class Test(TestCase):
    def test_sum(self):
        self.assertEqual(4, sum(2, 2))
