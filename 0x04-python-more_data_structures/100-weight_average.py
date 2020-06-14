#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    total = 0
    total_weight = 0

    for item in my_list:
        total += item[0] * item[1]
        total_weight += item[1]

    return total/total_weight
