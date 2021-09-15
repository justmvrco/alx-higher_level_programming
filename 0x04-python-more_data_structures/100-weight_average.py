#!/usr/bin/python3


# weight_average - returns the weighted average of all intergers tuple.
def weight_average(my_list=[]):
    if my_list:
        weight = 0
        denom = 0
        avg = 0
#    print(my_list[0][0])
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                weight += my_list[i][0] * my_list[i][1]
                denom += my_list[i][1]
        avg = weight / denom
        return avg
    return 0
