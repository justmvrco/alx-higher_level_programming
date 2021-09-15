#!/usr/bin/python3


# uniq_add - adds all unique integers in a list (only once for each integer.
def uniq_add(my_list=[]):
    unique = set(my_list)
    uniqueLi = list(unique)
    sum = 0

    for i in uniqueLi:
        sum += i
    return sum
