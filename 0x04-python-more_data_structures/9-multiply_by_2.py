#!/usr/bin/python3


# multiply_by_2 - returns a new dictionary with all values multiplied by two.
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i, j in new_dict.items():
        new_dict[i] = j*2
    return new_dict
