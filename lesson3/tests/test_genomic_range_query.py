from unittest import TestCase

from lesson3.GenomicRangeQuery import solution


class GenomicRangeQueryTestCase(TestCase):
    def test(self):
        self.assertEqual([2, 4, 1], solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
        self.assertEqual([1], solution('A', [0], [0]))
        self.assertEqual([1, 1, 2], solution('AC', [0, 0, 1], [0, 1, 1]))
        self.assertEqual([1, 3, 3, 4], solution('AAGT', [0, 2, 2, 3], [0, 2, 3, 3]))