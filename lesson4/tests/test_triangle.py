from unittest import TestCase

from lesson4.Triangle import solution


class TriangleTestCase(TestCase):
    def test(self):
        self.assertEqual(1, solution([10, 2, 5, 1, 8, 20]))
        self.assertEqual(0, solution([10, 50, 5, 1]))
        self.assertEqual(0, solution([1, 5]))
        self.assertEqual(0, solution([]))
