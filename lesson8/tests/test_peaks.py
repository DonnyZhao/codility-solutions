from unittest import TestCase

from lesson8.Peaks import solution


class PeaksTestCase(TestCase):
    def test(self):
        self.assertEqual(3, solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
        self.assertEqual(0, solution([5]))
        self.assertEqual(0, solution([1, 2, 3, 4, 5, 6]))
        self.assertEqual(0, solution([0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(7, solution([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
        self.assertEqual(4, solution([5, 6, 5, 6, 1, 1, 1, 1, 6, 5, 6, 5]))
        self.assertEqual(4, solution([1, 6, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 6, 1]))
