#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for i in range(0, len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            new_str += chr(ord(str[i]) - (ord('a') - ord('A')))
        else:
            new_str += str[i]

    print("{}".format(new_str))
