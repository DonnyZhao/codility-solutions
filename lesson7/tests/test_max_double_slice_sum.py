from unittest import TestCase

from lesson7.MaxDoubleSliceSum import solution


class MaxDoubleSliceSumTestCase(TestCase):
    def test(self):
        self.assertEqual(17, solution([3, 2, 6, -1, 4, 5, -1, 2]))
        self.assertEqual(10, solution([0, 10, -5, -2, 0]))
        self.assertEqual(1, solution([5, 0, 1, 0, 5]))
        self.assertEqual(18, solution([1, 3, 4, 2, -3, 4, -10, 1, 1, 4, -2, 4, 1]))
        self.assertEqual(0, solution([-4, -5, -1, -5, -7, -19, -11]))
        self.assertEqual(26, solution([6, 1, 5, 6, 4, 2, 9, 4]))
        self.assertEqual(0, solution([5, 5, 5]))