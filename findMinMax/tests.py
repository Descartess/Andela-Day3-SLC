import unittest
""" tests for min max """
from findMinMax import find_min_max

class TestMinMax(unittest.TestCase):
    def test_occurance_1(self):
        """ finding occurance 1"""
        minmax = find_min_max([1,2,4,8,])
        self.assertEqual([1,8],minmax)
