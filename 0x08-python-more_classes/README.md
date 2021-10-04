# 0x08-python-more_classes

This project entails more examples on how use classes in Python.

## 0-rectangle.py

An empty class ``` Rectangle ``` that defines a rectangle.

## 1-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
	* property ``` def width(self): ``` to retrieve it
	* property setter ``` def width(self, value): ``` to set it:
		- ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
		- if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
	* property ``` def height(self): ``` to retrieve it
	* property setter ``` def height(self, value): ``` to set it:
		- ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
		- if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```

## 2-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
	* if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*

## 3-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
	* if ``` width ``` or ``` height ``` is equal to *0*, return an empty string

## 4-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```

## 5-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```
- Print the message ``` Bye rectangle... (... are 3 dots not ellipsis) when an instance of Rectangle is deleted.

## 6-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Public class attribute ``` number_of_instances ```:
	* Initialized to *0*
	* Incremented during each new instance instantiation
	* Decremented during each instance deletion 
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```
- Print the message ``` Bye rectangle... (... are 3 dots not ellipsis) when an instance of Rectangle is deleted.

## 7-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Public class attribute ``` number_of_instances ```:
        * Initialized to *0*
        * Incremented during each new instance instantiation
        * Decremented during each instance deletion
- Public class attribute ``` print_symbol ``` :
	* Initialized to *#*
	* Used as symbol for string representation
	* Can be any type
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```
- Print the message ``` Bye rectangle... (... are 3 dots not ellipsis) when an instance of Rectangle is deleted.

## 8-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Public class attribute ``` number_of_instances ```:
        * Initialized to *0*
        * Incremented during each new instance instantiation
        * Decremented during each instance deletion
- Public class attribute ``` print_symbol ``` :
        * Initialized to *#*
        * Used as symbol for string representation
        * Can be any type
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```
- Print the message ``` Bye rectangle... (... are 3 dots not ellipsis) when an instance of Rectangle is deleted.
- Static method ``` def bigger_or_equal(rect_1, rect_2): ``` that returns the biggest rectangle based on the area
	* ``` rect_1 ```  must be an instance of ``` Rectangle ```, otherwise a ``` TypeError ``` exception with the message ``` rect_1 must be an instance of Rectangle ``` is raised.
	* ``` rect_2 ``` must be an instance of ``` Rectangle ```, otherwise a ``` TypeError ``` exception with the message ``` rect_2 must be an instance of Rectangle ``` is raised.
	* Returns ``` rect_1 ``` if both have the same area value.

## 9-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Public class attribute ``` number_of_instances ```:
        * Initialized to *0*
        * Incremented during each new instance instantiation
        * Decremented during each instance deletion
- Public class attribute ``` print_symbol ``` :
        * Initialized to *#*
        * Used as symbol for string representation
        * Can be any type
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```
- Print the message ``` Bye rectangle... (... are 3 dots not ellipsis) when an instance of Rectangle is deleted.
- Static method ``` def bigger_or_equal(rect_1, rect_2): ``` that returns the biggest rectangle based on the area
        * ``` rect_1 ```  must be an instance of ``` Rectangle ```, otherwise a ``` TypeError ``` exception with the message ``` rect_1 must be an instance of Rectangle ``` is raised.
        * ``` rect_2 ``` must be an instance of ``` Rectangle ```, otherwise a ``` TypeError ``` exception with the message ``` rect_2 must be an instance of Rectangle ``` is raised.
        * Returns ``` rect_1 ``` if both have the same area value.
- Class method ``` def square(cls, size=0): ``` that returns a new Rectangle instance with ``` width == height == size ```
