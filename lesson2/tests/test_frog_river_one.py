from unittest import TestCase

from lesson2.FrogRiverOne import solution


class FrogRiverOneTestCase(TestCase):
    def test(self):
        self.assertEqual(6, solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
        self.assertEqual(-1, solution(10, [1, 3, 1, 4, 2, 3, 5, 4]))