from unittest import TestCase

from lesson1.TapeEqulibrum import solution


class TapeEqulibrumTestCase(TestCase):
    def test(self):
        self.assertEqual(1, solution([3, 1, 2, 4, 3]))