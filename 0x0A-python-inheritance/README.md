# 0x0A-python-inheritance


## 0-lookup.py

A function that returns the list of availbale attributes and methods of an object.

- Prototype: ``` def lookup(obj): ```.
- Return: a list object.

## 1-my_list.py

A class MyList tat inherits from list.

- Public instance method: ``` def print_sorted(self): ``` that prints the list, but sorted (ascending sort).
- Assumption: all elements of list aree of type ``` int ```.

## 2-is_same_class.py

A function that returns ``` True ``` if the object is *exactly* an instance of the specified class, otherwise ``` False ```.

- Prototype: ``` def is_same_class(obj, a_class):

## 3-is_kind_of_class.py

A function that returns ``` True ``` if teh object is an instance of, or if the object is an instance of a class that inherited from the specified class. Otherwise return ``` False ```.

- Prototype: ``` def is_kind_of_class(obj, a_class): ```

## 4-inherits_from.py

A function that returns ``` True ``` if the object is an instance of a class that inherited (directly or indirectly) from the specified class. Otherwise ``` False ```.

- Prototype: ``` def inherits_from(obj, a_class): ```

## 5-base_geometry.py

An empty class ``` BaseGeometry ```.

## 6-base_geometry.py

A class ``` BaseGeometry ``` (based on 5-base_geometry.py).

- Public instance method: ``` def area(self): ``` raises an Exception with the message ``` area() is not implemented ```.

## 7-base_geometry.py

A class BaseGeometry (based on 6-base_geometry.py).

- Public instance method: ``` def area(self): ``` raises an Exception with the message ``` are    a() is not implemented ```.
- Public instance method: ```def integer_validator(self, name, value):``` that validates ``` value ```:
	* Assumption: ``` name ``` is always a string.
	* If ``` value ``` is not an integer: ``` TypeError ``` with te message ``` <name> must be an integer ``` is raised.
	* If ``` value ``` is less or equal to 0: ``` ValueError ``` exception with the message ``` <name> must be greater than 0 ```.

## 8-rectangle.py

A class ``` Rectangle ``` that inherits from ``` BaseGeometry ``` (7-base_gometry.py)

- Instantiation with ``` width ``` and ``` height ```: ``` def __init__(self, width, height): ```:
	* ``` width ``` and ``` height ``` must be private. No getter or setter.
	* ``` width ``` and ``` height ``` must be positive integers, validated by integer_validator.


## 9-rectangle.py

A class ``` Rectangle ``` that inherits from ``` BaseGeometry ``` (7-base_gometry.py)

- Instantiation with ``` width ``` and ``` height ```: ``` def __init__(self, width, height):     ```:
         * ``` width ``` and ``` height ``` must be private. No getter or setter.
	 * ``` width ``` and ``` height ``` must be positive integers, validated by integer_validator.
- the ``` area() ``` method has been implemented.
- ``` print() ``` should print, and ``` str() ``` return the following rectangle description: ``` [Rectangle] <width>/<height> ```.


## 10-square.py

A class ``` Square ``` that inherits from ``` Rectangle ``` (9-rectangle.py):

- Instantiation with ``` size: def __init__(self, size): ```
	* ``` size ``` must be private. No getter or setter.
	* ``` size ``` must be a positive integer, validated by ``` integer validator ```.
- the ``` area() ``` method is implemented.

## 11-square.py

A class ``` Square ``` that inherits from ``` Rectangle ``` (9-rectangle.py):

- Instantiation with ``` size: def __init__(self, size): ```
	* ``` size ``` must be private. No getter or setter.
	* ``` size ``` must be a positive integer, validated by ``` integer validator ```.
- the ``` area() ``` method is implemented.
- ``` print() ``` should print, and ``` str() ``` return the following rectangle description:``` [Square] <width>/<height> ```.

## 100-my_int.py

A class ``` MyInt ``` that inherits from ``` int ```:

- ``` MyInt ``` has ``` ==``` and ``` != ``` inverted

## 101-add_attribute.py

A function that adds a new attribute to an object if its possible.

- A ``` TypeError ``` exception with the message ``` can't add new attribute ``` is raised when the object can't have the new attribute.

