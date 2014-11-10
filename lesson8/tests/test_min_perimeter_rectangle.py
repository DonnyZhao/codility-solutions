from unittest import TestCase

from lesson8.MinPerimeterRectangle import solution


class MinPerimeterRectangleTestCase(TestCase):
    def test(self):
        self.assertEqual(22, solution(30))
        self.assertEqual(4, solution(1))
        self.assertEqual(24, solution(36))
        self.assertEqual(28, solution(48))
        self.assertEqual(204, solution(101))
        self.assertEqual(1238, solution(1234))