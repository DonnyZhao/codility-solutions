from unittest import TestCase

from lesson7.MaxProfit import solution


class MaxProfitTestCase(TestCase):
    def test(self):
        self.assertEqual(356, solution([23171, 21011, 21123, 21366, 21013, 21367]))
        self.assertEqual(3, solution([4, 3, 2, 1, 2, 3, 4]))
        self.assertEqual(0, solution([5, 4, 3, 2, 1]))
        self.assertEqual(0, solution([]))
        self.assertEqual(99000, solution([1000, 100000, 0, 1000, 2000, 3000]))
        self.assertEqual(3, solution([8, 9, 3, 6, 1, 2]))