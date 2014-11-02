from unittest import TestCase

from lesson2.MaxCounters import solution


class MaxCountersTestCase(TestCase):
    def test(self):
        self.assertEqual([3, 2, 2, 4, 2], solution(5, [3, 4, 4, 6, 1, 4, 4]))
        self.assertEqual([1], solution(1, [1, 2, 4]))