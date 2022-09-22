#!/usr/bin/python3
from sys import argv as argv
length = len(argv)
if length == 1:
    print("{} arguments.".format(length - 1))
elif length == 2:
    print("{} argument:".format(length - 1))
    for i in range(1, length):
        print("{0}: {1}".format(i, argv[i]))
elif length > 2:
    print("{} arguments:".format(length - 1))
    for i in range(1, length):
        print("{0}: {1}".format(i, argv[i]))
