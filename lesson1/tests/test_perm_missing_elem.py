from unittest import TestCase

from lesson1.PermMissingElem import solution


class PermMissingElemTestCase(TestCase):
    def test(self):
        self.assertEqual(4, solution([2, 3, 1, 5]))
        self.assertEqual(1, solution([2, 3, 4, 5]))
        self.assertEqual(1, solution([]))
        self.assertEqual(1, solution([2]))