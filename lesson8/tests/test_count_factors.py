from unittest import TestCase

from lesson8.CountFactors import solution


class CountFactorsTestCase(TestCase):
    def test(self):
        self.assertEqual(8, solution(24))
        self.assertEqual(5, solution(16))
        self.assertEqual(1, solution(1))
        self.assertEqual(2, solution(41))
        self.assertEqual(4, solution(69))
        self.assertEqual(30, solution(720))
        self.assertEqual(60, solution(5040))
        self.assertEqual(4, solution(34879))
