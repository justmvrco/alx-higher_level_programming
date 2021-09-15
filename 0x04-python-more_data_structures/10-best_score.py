#!/usr/bin/python3


# best_score - retuns a key with the biggest integer value
def best_score(a_dictionary):
    if a_dictionary:
        dlist = list(a_dictionary)
        largK = dlist[0]
        for i in dlist:
            if a_dictionary[largK] < a_dictionary[i]:
                largK = i
        return largK
    else:
        return
