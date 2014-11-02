from unittest import TestCase

from lesson3.CountDiv import solution


class CountDivTestCase(TestCase):
    def test(self):
        self.assertEqual(3, solution(6, 11, 2))
        self.assertEqual(61499951, solution(100, 123000000, 2))