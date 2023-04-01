#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of"
b = "is"
if number > 0:
    last_digit = number % 10
    if last_digit > 5:
        print("{}{:d} {} {:d} and is greater than 5".format(a, number, b, last_digit))
    elif last_digit == 0:
        print("{} {:d} {} {:d} and is 0".format(a, number, b, last_digit))
    else:
        print("{} {:d} {} {:d} and is less than 6 and not 0".format(a, number, b, last_digit))
elif number < 0:
    last_digit = -1 * number % 10
    print("{} {:d} {} {:d} and is less than 6 and not 0".format(a, number, b, -last_digit))
else:
    last_digit = 0
    print("{} {:d} {} {:d} and is 0".format(a, number, b, last_digit))
