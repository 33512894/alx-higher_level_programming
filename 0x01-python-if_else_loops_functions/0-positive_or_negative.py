#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print(number, "is negative")
if number == 0:
    print(number, "is zero")
else:
    if number > 0:
        print(number, "is positive")
