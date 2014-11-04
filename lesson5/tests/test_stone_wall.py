from unittest import TestCase

from lesson5.StoneWall import solution


class StoneWallTestCase(TestCase):
    def test(self):
        self.assertEqual(4, solution([1, 2, 4, 8, 8, 8, 4, 2, 1]))
        self.assertEqual(5, solution([1, 1, 1, 2, 3, 3, 2, 1, 2, 3, 3, 3]))
        self.assertEqual(7, solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
        self.assertEqual(3, solution([1, 2, 3, 3, 2, 1]))
        self.assertEqual(8, solution([2, 5, 1, 4, 6, 7, 9, 10, 1]))
        self.assertEqual(3, solution([3, 2, 1]))
        self.assertEqual(1, solution([1]))