#!/usr/bin/python3


# complex_delete - delets keys with a specific value in a dictionary.
def complex_delete(a_dictionary, value):
    keylist = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if value == val:
                keylist.append(key)

        for kl in keylist:
            if kl in a_dictionary:
                del a_dictionary[kl]
    return a_dictionary
