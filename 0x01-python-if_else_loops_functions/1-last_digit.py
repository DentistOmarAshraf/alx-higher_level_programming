#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
str1 = "Last digit of"
str2 = "greater than 5"
str3 = "less than 6 and not 0"
if number >= 0:
    n = number % 10
if number < 0:
    n = number % -10
if n > 5:
    print("{:s} {:d} is {:d} and is {:s}".format(str1, number, n, str2))
if n == 0:
    print("{:s} {:d} is {:d} and is 0".format(str1, number, n))
if n < 6 and n != 0:
    print("{:s} {:d} is {:-d} and is {:s}".format(str1, number, n, str3))
