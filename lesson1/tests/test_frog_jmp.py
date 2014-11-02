from unittest import TestCase

from lesson1.FrogJmp import solution


class FrogJmpTestCase(TestCase):
    def test(self):
        self.assertEqual(3, solution(10, 85, 30))