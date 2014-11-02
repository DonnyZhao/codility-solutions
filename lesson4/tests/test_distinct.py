from unittest import TestCase

from lesson4.Distinct import solution


class DistinctTestCase(TestCase):
    def test(self):
        self.assertEqual(3, solution([2, 1, 1, 2, 3, 1]))