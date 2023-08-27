#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for value, weight in my_list:
        numerator += value * weight
        denominator += weight

    return numerator / denominator
