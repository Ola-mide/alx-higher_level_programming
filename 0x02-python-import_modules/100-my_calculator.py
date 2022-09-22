#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as argv
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if length == 4:
        if argv[2] not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            if argv[2] == "+":
                result = add(a, b)
            elif argv[2] == "-":
                result = sub(a, b)
            elif argv[2] == "*":
                result = mul(a, b)
            elif argv[2] == "/":
                result = div(a, b)
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
