import unittest
from calc import aec_divide, aec_subtract
import sys

class TestCalculator(unittest.TestCase):

    def test_divide(self):
        arg_ints = [20, 5]
        div_result = aec_divide(arg_ints)
        self.assertEqual(div_result, 4)


    def test_divide_by_zero(self):
        arg_ints = [10, 0]
        div_result = aec_divide(arg_ints)
        self.assertEqual(div_result, 0)  


    def test_subtract_more_than_two_args(self):
        arg_ints = [20, 5, 3]
        with self.assertRaises(ValueError):
            aec_subtract(arg_ints)


    def test_divide_more_than_two_args(self):
        arg_ints = [20, 5, 2]
        with self.assertRaises(ValueError):
            aec_divide(arg_ints)

if __name__ == '__main__':
    unittest.main()