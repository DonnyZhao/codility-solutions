from unittest import TestCase

from lesson2.PermCheck import solution


class PermCheckTestCase(TestCase):
    def test(self):
        self.assertEqual(1, solution([4, 1, 3, 2]))
        self.assertEqual(0, solution([1, 1, 4, 4]))
        self.assertEqual(0, solution([4, 1, 3]))