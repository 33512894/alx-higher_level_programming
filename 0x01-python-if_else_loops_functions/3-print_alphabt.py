for ASCII in range(ord('a'), ord('z') + 1):
    if chr(ASCII) not in ['q', 'e']:
        print(chr(ASCII), end="")
