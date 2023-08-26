#!/usr/bin/python3
import sys

number_args = len(sys.argv) - 1

print("Number of argument(s):", number_args, end="")

if number_args == 1:
    print(" argument:", end="")
else:
    print(" arguments:", end="")
if number_args > 0:
    print(":")

for i in range(number_args):
    print(i + 1, ":", sys.argv[i + 1])

if number_args > 0:
    print()
