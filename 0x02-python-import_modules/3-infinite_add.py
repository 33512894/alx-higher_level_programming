#!/usr/bin/python3
import sys

sum_args = 0

for arg in sys.argv[1:]:
    sum_args += int(arg)

print(sum_args)
