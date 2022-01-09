#!/usr/bin/python3
"""
    Function: find_peak(listint)
"""


def find_peak(listint):
    """
        finds a peak in a list of unsorted integers
        Args:
            listint (list)
        Return:
            peak
    """
    listint = listint.copy()

    length = len(listint)

    if length == 0:
        return

    # find index of element in middle
    mid = int(length/2)

    # compare mid index element with neighbours if they exist
    if (mid == 0 or listint[mid - 1] <= listint[mid]) and (mid == length - 1
                                                           or listint[mid + 1]
                                                           < listint[mid]):
        return listint[mid]
    elif mid > 0 and listint[mid - 1] > listint[mid]:
        return find_peak(listint[:mid])
    else:
        return find_peak(listint[mid:])
