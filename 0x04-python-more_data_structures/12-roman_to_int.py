#!/usr/bin/python3

def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return max_list - to_sub

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_num = [0]
    num = 0
    last_rom = 0

    for ch in roman_string:
        if ch in rom_n:
            value = rom_n[ch]
            if value <= last_rom:
                num += to_subtract(list_num)
                list_num = [value]
            else:
                list_num.append(value)
            last_rom = value

    num += to_subtract(list_num)

    return num
