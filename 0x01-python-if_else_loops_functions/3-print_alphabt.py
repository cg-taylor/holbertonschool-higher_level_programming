#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char == ord('e') or char == ord('q'):
        continue
    else:
        print('{:c}'.format(char), end='')
