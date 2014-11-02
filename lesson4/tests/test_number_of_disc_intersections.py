from unittest import TestCase

from lesson4.NumberOfDiscIntersections import solution


class NumberOfDiscIntersectionsTestCase(TestCase):
    def test(self):
        self.assertEqual(11, solution([1, 5, 2, 1, 4, 0]))
        self.assertEqual(15, solution([3, 3, 3, 5, 1, 2]))
        self.assertEqual(5, solution([1, 10, 100, 1]))
        self.assertEqual(6, solution([1, 0, 1, 0, 1]))
        self.assertEqual(0, solution([]))
        self.assertEqual(41, solution([1, 5, 8, 7, 8, 4, 8, 5, 0, 5]))
        self.assertEqual(176, solution([12, 4, 20, 19, 9, 13, 4, 4, 6, 14, 4, 20, 1, 4, 1, 16, 7, 9, 6, 13]))
        self.assertEqual(1169, solution([7, 31, 8, 36, 30, 19, 31, 28, 2, 27, 31, 26, 44, 37, 19, 11, 6, 41, 35, 31, 22, 25, 11, 27, 7, 31, 32, 34, 12, 4, 16, 35, 26, 38, 21, 20, 46, 8, 10, 30, 32, 22, 28, 22, 34, 45, 42, 32, 23, 48]))
        self.assertEqual(2, solution([1, 2147483647, 0]))