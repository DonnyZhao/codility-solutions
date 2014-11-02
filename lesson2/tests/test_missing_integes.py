from unittest import TestCase

from lesson2.MissingIntegers import solution


class MissingIntegersTestCase(TestCase):
    def test(self):
        self.assertEqual(5, solution([1, 3, 6, 4, 1, 2]))
        self.assertEqual(1, solution([2147413647]))
        self.assertEqual(6, solution([2147413647, 1, 2, 3, 4, 5, -2147413647]))
        self.assertEqual(2, solution([1]))
        self.assertEqual(7, solution([1, 3, 6, 4, 1, 2, 5, 8, 9]))
        self.assertEqual(5, solution([1, 3, 0, -10, 6, 4, 1, 2]))
        self.assertEqual(1, solution([-5, -2, -2, 0]))