# PYTHON DATA STRUCTURES

This project introduces python data structures.

## 0-print_list_integer.py

This file conatins a fu nction that prints all integers of a list.
- Prototype: ``` def print_list_integer(my_list=[]): ```
- Format: one integer per line.

## 1-element_at.py

This file contains a function that retrieves an elemnt from a list.
- Prototype: ``` def element_at(my_list, idx): ```
- Return:
	* *None* if idx is negative or out of range.
	* Number retrieved.

## 2-replace_in_list.py

This file contains a function that replaces an element of a list at a specific position.
- Prototype: ``` def replace_in_list(my_list, idx, element): ```.
- Return:
	* Original list if idx is negative or out of range.
	* Modified list.

## 3-print_reversed_list_integer.py

This file contains a function that prints all integers of a a list, in reverse order.
- Prototype: ``` def print_reversed_list_integer(my_list=[]):
- Format: one integer per line.

## 4-new_in_list.py

This file contains a function that replaces an element in a list at a specific position without modifying the original list.
- Prototype: ``` def new_in_list(my_list, idx, element): ```.
- Return:
	* A copy of the origin list if idx is negative or less than zero.
	* The modified copy of the string.

## 5-no_c.py

This file contains a function that removes all characters c and C froma string.
- Prototype: ``` def no_c(my_string): ```
- Return:
	* New string.

## 6-print_matrix_integer.py

This file conatins a function that prints a matrix of integers.
- Prototype: ``` def print_matrix_integer(matrix=[[]]): ```
- Format: x x x
	  x x x
	  x x x

## 7-add_tuple.py

This file contains a function that adds two tuples.
- Prototype: ``` def add_tuple(tuple_a=(), tuple_b()): ```
- Return:
	* A tuple with two integers such that:
		- The first element is the sum of the first elemeent of each tuple.
		- The Second element is the sum of the second element of each tuple.
	* If a tuple is smaller tha 2, value 0 is used for each missing integer.
	* If a tuple is bigger than 2, only the first two integers are used.
