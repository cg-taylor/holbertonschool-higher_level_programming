#!/usr/bin/python3

# print ASCII alphabet backwards alternating lower and uppercase letters
# no newline at end of print
# one loop, one print, no hard coded variables, no modules
# Output: zYxWvUtSrQpOnMlKjIhGfEdCbA

# z - Y == 33, x - W == 33, v - U == 33, ...

for letter in range(ord('z'), ord('a'), -2):
    print("{:c}{:c}".format(letter, letter - 33), end="")
