#!/usr/bin/python3
"""
    5-save_to_json_file: save_to_json_file()
"""


import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file using JSON rep.
        Args:
            my_obj (object): object to be serialized.
            filename (str): name of file where string is stored.
    """
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)
