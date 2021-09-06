# *alx-higher_level_programming*

*INTRODUCTION*

Entering the exciting world of High Level Programming, where we experience strong
 abstraction hence shorter programs. What's even more exciting is the use of an
 interpretor.

 This repository contains programs written in Python, C and Shell.

*PROJECTS*

## 1. 0x00-python-hello_world

Getting started with Python. Formating output and string manipulation.

## 2. 0x01-python-if_else_loops_functions

Loops and flow control using if...else. Functions in python are also introduced here.

## 3. 0x02-python-import_modules

Python modules enhance code reusability. This project explains how modules are created and used to write python scripts.

## 4. 0x03-python-data_structures

Python supports a number of data structures. These include lists, stacks queues, tuples.

## 5. 0x04-python-more_data_structures

More data structures in python are sets and dictionaries. In built function introduced here include map, filter, lambda anonymous functions.

## 6. 0x05-python-exceptions

An exception is an error detected during execution. Python offers a variety of builtin exceptions and also allows for custom exceptions.

## 7. 0x06-python_classes

Object Oriented Programming is a way of organizing a program such that the data and functionality are put together to make an object. 
An object is an instance of a class whereby the class defines the layout of te object in terms of the attributes and methods.
Python like any other OOP Language, supports the four main concepts of OOP. These are: Data Encapsulation, Data Abstraction, Inheritance and Polymorphism.

## 8. 0x07-python-test_driven_development

Test driven development involves coming up with tests for a certain program before writing the actual program. Pyhtonn has made this possible through the *doctest* module. 
The *doctest* module searches or pieces of text that lok like interactive Pythonn sessions and then executes those sessions to verify tay work exactly as shown. 

## 9. 0x08-python-more_classes

More class example tasks in Python.

## 10. 0x09-python-everything_is_object

Pyton works differently with different types of objects. It is necessary to understand the reason why this is so.

## 11. 0x0A-Python - Inheritance

Inheritance is the procedure in which one class inherits the attributes and methods of another class.
In python 3, if there is no explicit superclass provided, a class will automatically inherit from object. 
The key terms in inheritance are:
- Superclass / Parent class: a class being inherited from.
- Subclass: a class inheriting from a superclass. It may be said to be derived from te parent or extends from te parent.

This project outlines some of the ways inheritance is implemented in Python.

## 12. 0x0B-Python - Input/Output

There are several ways to presebt the output of a program ie In human-readable form or writing to a file for future use.
While we've already encountered ``` print() ``` and ``` write() ```, there are functions that python offers that add to these. These functions work directly with either text or binary files.


## 13. 0x0C-python-almost_a_circle

This project reviews everything about Python:

	- Import
	- Exceptions
	- Class
	- Private attribute
	- Getter/Setter
	- Class method
	- Static method
	- Inheritance
	- Unittest
	- Read/Write file
	- args and kwargs
	- Serialization/Deserialization
	- JSON

## 14. 0x0D-SQL_introduction

SQL - Structured Query Language.
MySQL is one of the major Database Management Systems available on open source.
Concepts touched on include:
* DDL and DML
* RA
* Functions
* Queries
* Subqueries
* User Management on MySQL
	- Creation of New Users
	- Grant Permissions
	- Revoke permissions
	- Deletion of Users
* Basic Query operations:
	- Joins
	- DISTINCT 
	- Unions
	- minus
* Relational Database model design
	- Design
	- Normalization
	- Entity Relationship Modeling

## 15. 0x12-javascript-warm_up

JavaScript is a programming language that adds interactiviy to a website. It was invented by Brendan Eich (co-founder of the Mozilla project, the Mozilla Foundation, and the Mozilla Corporation).
The concepts covered in this project are:
* How to run JavaScript
* Creating variables and constants
* Difference between *var*, *let* and *const*
* The datatypes available in JavaScript.
* Control Structures: *if, if ... else *
* Comments
* Loops
* Break and Continue Statements
* Functions and how to use them, the different return values.
* Scope of variables
* Arithmetic Operators and how to use them.
* Manipulate dictionary.
* Import a file.


## 16. 0x13-javascript_objects_scopes_closures

This is a continuation of the JavaScript basics. Concepst practiced here are:
* Creating an object in JavaScript.
* *this* - what it means and how to use it.
* *undefined* - what it means.
* Variable type or scope
* Closure
* Prototype
* Inheriting an object from another.

## 17. 0x0F-python-object_relational_mapping

This project demonstrates how to link Databases and Python.
It will cover how to use the module ``` MySQLdb ``` to connect to a MySQL database and execute querries and how to use the module ``` SQLAlchemy ``` and Object Relational Mapper(ORM).

The biggest difference between the two is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without an ORM you will do this:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

with an ORM you will only need to do this: 
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

However, the biggest difficulty with an ORM is the syntax. It differs from one ORM to another.

## 18. 0x10-python-network_0

This project describes some ways to use curl to debug.
As well as :
- HTTP
- HTTP Cookies

## 19. 0x11-python-network_1

Using Python's ```urllib``` package to fetch URLS 
- [urllib.request](https://docs.python.org/3/howto/urllib2.html)

## END MAYBE
