#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = -(-number - ((-number // 10) * 10))
elif number >= 0:
    last_digit = (number - ((number // 10) * 10))

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
