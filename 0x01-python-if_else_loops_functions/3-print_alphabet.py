#!/usr/bin/python3
for char_ascii in range(ord('a'), ord('z') + 1):
    if chr(char_ascii) not in ['q', 'e']:
        print(chr(char_ascii), end="")
