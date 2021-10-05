"""
    unit test for 6-max_integer.py
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([4, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([8, 234, 332, 33]), 332)
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
        self.assertAlmostEqual(max_integer([20000000022]), 20000000022)
        self.assertAlmostEqual(max_integer([]), None)

    def test_non_int(self):
        self.assertRaises(TypeError, max_integer, True)
