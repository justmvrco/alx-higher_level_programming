#!/usr/bin/python3
"""
    10-student: class Student
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
            reload_from_json - replaces a;; attributes of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student Instance.
            Args:
                json (dictionary): reload data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
