#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[:x]:
            print("{}".format(i), end="")
            count += 1
    except:
        pass
    print()
    return count
