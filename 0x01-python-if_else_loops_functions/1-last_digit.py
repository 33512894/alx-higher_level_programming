#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    print("last digit of", number, "is", last_digit, "and is greater than 5")
if last_digit < 6 and last_digit != 0:
    print("last digit of", number, "is", last_digit, "is less than 6 and is not 0")
else:
    if last_digit < 6 and last_digit == 0:
       print("last digit of", number, "is", last_digit, "is less than 6 and is 0")