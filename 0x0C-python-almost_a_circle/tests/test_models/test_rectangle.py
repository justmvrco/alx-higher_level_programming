"""
    unit test for models/rectangle.py
"""
import json
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Testing rectangle
    """
    def setUp(self):
        """
            Initialize an insatnce of rectangle.
            With width and height only.
        """
        self.r = Rectangle(20, 10)

    def tearDown(self):
        """
            Deleting created instance
        """
        del self.r

    def test_width(self):
        """
            Testing rectangle width getter
        """
        self.assertEqual(20, self.r.width)

    def test_height(self):
        """
            Testing the height getter
        """
        self.assertEqual(10, self.r.height)

    def test_x(self):
        """
            Testing the x getter
        """
        self.r.x = 2
        self.assertEqual(2, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        """
            Testing the y getter
        """
        self.r.y = 2
        self.assertEqual(2, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_rectangle_id(self):
        """
            Testing the id of the rectangle
        """
        r1 = Rectangle(1, 3, 0, 0, 12)
        self.assertEqual(12, r1.id)

    def test_width_str(self):
        """
            Testing wrong type for width: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("w", 5)

    def test_width_list(self):
        """
            Testing wrong type for width: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle([1, 2], 8)

    def test_width_bool(self):
        """
            Testing wrong type for width: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 9)

    def test_height_str(self):
        """
            Testing wrong type for height: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, "h")

    def test_height_list(self):
        """
            Testing wrong type for height: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(8, [1, 2])

    def test_height_bool(self):
        """
            Testing wrong type for height: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(9, True)

    def test_x_str(self):
        """
            Testing wrong type for x: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "x", 0)

    def test_x_list(self):
        """
            Testing wrong type for x: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, [1, 2], 8)

    def test_x_bool(self):
        """
            Testing wrong type for x: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, True, 9)

    def test_y_str(self):
        """
            Testing wrong type for y: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 0, "y")

    def test_y_list(self):
        """
            Testing wrong type for y: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 6, [1, 2])

    def test_y_bool(self):
        """
            Testing wrong type for y: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 9, True)

    def test_width_negative(self):
        """
            Testing negative value for width
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-2, 8)

    def test_width_zero(self):
        """
            Testing zero value for width
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 8)

    def test_height_negative(self):
        """
            Testing negative vale fro height
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(8, -2)

    def test_height_zero(self):
        """
            Testing zero value for height
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(8, 0)

    def test_x_negative(self):
        """
            Testing negative value for x
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -1, 0)

    def test_y_negative(self):
        """
            Testing negative value for y
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 4, -7)

    def test_width_float(self):
        """
            testing for float
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1.07, 5)

    def test_height_float(self):
        """
            testing for float
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 1.07)

    def test_x_float(self):
        """
            testing for float
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 8, 1.07)

    def test_y_float(self):
        """
            testing for float
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 8, 1.07)

    def test_area(self):
        """
            Testing the rectangle area
        """
        r1 = Rectangle(12, 2)
        self.assertEqual(r1.area(), 24)

    def test_update_id(self):
        """
            Testing the update id
        """
        r1 = Rectangle(10, 1)
        r1.update(12)
        self.assertEqual(12, r1.id)

    def test_update_width(self):
        """
            Testing update width
        """
        r1 = Rectangle(1, 2)
        r1.update(2, 12)
        self.assertEqual(12, r1.width)

    def test_update_height(self):
        """
            Testing update height
        """
        r1 = Rectangle(1, 3)
        r1.update(2, 3, 4)
        self.assertEqual(4, r1.height)

    def test_update_x(self):
        """
            Testing update x
        """
        r1 = Rectangle(1, 2)
        r1.update(2, 3, 4, 5)
        self.assertEqual(5, r1.x)

    def test_update_y(self):
        """
            Testing update y
        """
        r1 = Rectangle(1, 2)
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual(6, r1.y)

    def test_update_dict(self):
        """
            Testing teh update method with kwargs
        """
        r1 = Rectangle(1, 3)
        r1.update(id=3, height=5, width=6, x=7, y=9)
        self.assertEqual(6, r1.width)

    def test_to_dict(self):
        """
            Testing to dict function return type
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_value(self):
        """
            Testing the dict function actual return value
        """
        r1 = Rectangle(1, 2, 0, 0, 345)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
                         {'height': 2, 'width': 1, 'id': 345, 'x': 0, 'y': 0})

    def test_missing_width(self):
        """
            Testing instance creation with no width value
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_missing_height(self):
        """
            Testing instance creation with no height value
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_overload_str(self):
        """
            Testing override str.
        """
        r1 = Rectangle(1, 2, 3, 4, 76)
        self.assertEqual("[Rectangle] (76) 3/4 - 1/2", r1.__str__())

    def test_display_no_xy(self):
        """
            Testing the display() without x and y
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(1, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "#\n#\n")

    def test_display_no_y(self):
        """
            Testing display() without y
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(1, 2, 1)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), " #\n #\n")

    def test_display_no_x(self):
        """
            Testing display() without x
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(1, 2, 0, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n#\n#\n")

    def test_display_xy(self):
        """
            Testing display() with x and y values
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(1, 2, 3, 4)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n\n\n   #\n   #\n")

    def test_create_dict_equal(self):
        """
            Testing creating rectangle is not equal
        """
        r1 = Rectangle(1, 2, 3, 5, 6)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_dict_is(self):
        """
            Testing create rectangle is (r1 is r2)
        """
        r1 = Rectangle(1, 2, 3, 5, 6)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    def test_save_to_file_none(self):
        """
            Testing save to file none
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_empty(self):
        """
            Testing save to file empty list
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_rect(self):
        """
            Testing save to file with proper input
        """
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(json.loads(content), [{"id": 5,
                                                    "width": 1, "height": 2,
                                                    "x": 3, "y": 4}])

    def test_save_to_file_noargs(self):
        """
            Testing save to file with no arguments
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_type(self):
        """
            Testing save to file , format saved in
        """
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(str, type(content))
