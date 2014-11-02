from unittest import TestCase

from lesson4.MaxProductOfThree import solution


class MaxProductOfThreeTestCase(TestCase):
    def test(self):
        self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))
        self.assertEqual(-80, solution([-10, -2, -4]))
        self.assertEqual(105, solution([4, 7, 3, 2, 1, -3, -5]))
        self.assertEqual(125, solution([-5, 5, -5, 4]))