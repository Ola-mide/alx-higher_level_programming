#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        num = ord(ch)
        print("{}".format(chr(num-32)if num in range(97, 123) else ch), end='')
    print('\n', end='')
