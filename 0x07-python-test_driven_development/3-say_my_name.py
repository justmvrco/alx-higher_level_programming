#!/usr/bin/python3
"""
    3-say_my_name: say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name prints My name is <first_name> <last_name>
        Args:
            first_name (string): the 1st name
            last_name (string): the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
