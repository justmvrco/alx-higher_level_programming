#!/usr/bin/python3
"""
    unit test for the class Rectangle
"""
import unittest
Rectangle = __import__('1-rectangle').Rectangle


class TestClassRectangle(unittest.TestCase):
    """
        test class for the Rectangle class instances
    """
    def test_type_class(self):
        """
            Checks the class of the instance
        """
        r = Rectangle()
        self.assertIsInstance(r, Rectangle)

    def test_typeError(self):
        """
            Checks for typeerrors raised
        """
        with self.assertRaises(TypeError):
            r = Rectangle("hi", 5)

        with self.assertRaises(TypeError):
            r = Rectangle(5, "hi")

    def test_valueError(self):
        """
            checks for value errors raised
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 9)
        with self.assertRaises(ValueError):
            r = Rectangle(9, -5)

    def test_noarguments(self):
        """
            checks for when no arguments are passed
        """
        r = Rectangle()
        
        self.assertAlmostEqual(r.width, 0)
        self.assertAlmostEqual(r.height, 0)
