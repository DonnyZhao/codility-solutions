from unittest import TestCase

from lesson3.ParssingCars import solution


class PassingCarsTestCase(TestCase):
    def test(self):
        self.assertEqual(5, solution([0, 1, 0, 1, 1]))