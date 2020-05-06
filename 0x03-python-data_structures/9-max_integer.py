#!/usr/bin/python3


def max_integer(my_list):
    max_val = 0
    current = 0

    if not my_list:
        return None

    for i in range(len(my_list)):
        current = my_list[i]
        if current > max_val:
            max_val = current

    return max_val
