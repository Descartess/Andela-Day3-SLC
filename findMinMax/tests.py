""" tests for find_min_max """
import unittest
from findMinMax import find_min_max

class TestMinMax(unittest.TestCase):
    """ methods for testing find_min_max"""
    def test_positive(self):
        """ test return values for all positive"""
        minmax = find_min_max([1,2,4,8,])
        self.assertEqual([1,8],minmax)
    def test_negative(self):
        """ test return values for all negative"""
        minmax = find_min_max([-1,-2,-4,-8,])
        self.assertEqual([-8,-1],minmax)
    def test_two_values(self):
        """test return two values """
        minmax = find_min_max([4,1])
        self.assertEqual([1,4],minmax)
    def test_same_value(self):
        """test return for same value"""
        minmax = find_min_max([4,4,4,4])
        self.assertEqual([1,4],minmax)




unittest.main()
