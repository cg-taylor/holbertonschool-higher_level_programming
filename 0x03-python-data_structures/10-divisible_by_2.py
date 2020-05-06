#!/usr/bin/python3


def divisible_by_2(my_list):
    test_result = my_list.copy()

    if not my_list:
        return None

    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            test_result[i] = 1
        else:
            test_result[i] = 0
        i += 1

    return test_result
