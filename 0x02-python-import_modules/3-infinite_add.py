#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as argv
    sum = 0
    index = 1
    length = len(argv)
    while index < length:
        sum += int(argv[index])
        index += 1
    print(sum)
