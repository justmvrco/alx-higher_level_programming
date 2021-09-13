#!/usr/bin/python3


# Function retrieves an elemnt from the liist
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
