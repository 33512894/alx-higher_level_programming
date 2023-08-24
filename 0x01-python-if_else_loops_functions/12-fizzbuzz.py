#!/usr/bin/python3
def fizzbuzz():
    for numb in range(1, 101):
        if numb % 3 == 0 and numb % 5 == 0:
            print("FizzBuzz ", end="")
        if numb % 3 == 0:
            print("Fizz ", end="")
        if numb % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numb), end="")
