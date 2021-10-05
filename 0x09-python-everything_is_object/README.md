# 0x09-python-everything_is_object

## Background context

Everything is an object. Python works differently with different types of objects. Example:
Modifying a variable:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```
Here b remains as the initial value of a , even thought a has changed.

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```
l is a list, it is assigned to m (making it a list). A change in either, is reflected on both.
This concept is known as aliasing, l and m refer to the same object (the list).


This projects shows different ways python deals with objects.

## Tasks

### 0-answer.txt

The file contains the function used to print the type of an object.

