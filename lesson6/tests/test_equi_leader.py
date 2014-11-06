from unittest import TestCase

from lesson6.EquiLeader import solution


class EquiLeaderTestCase(TestCase):
    def test(self):
        self.assertEqual(0, solution([1000000000]))
        self.assertEqual(2, solution([4, 3, 4, 4, 4, 2]))
        self.assertEqual(1, solution([0, 0]))
        self.assertEqual(3, solution([4, 4, 2, 5, 3, 4, 4, 4]))
        self.assertEqual(79, solution([0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]))