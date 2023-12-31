#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    num = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for j in roman_string:
        num += digits.get(j, 0)
    subs = {'CM': -200, 'CD': -200, 'XC': -20, 'XL': -20, 'IX': -2, 'IV': -2}
    chars = ""
    for j in range(0, len(roman_string) - 1):
        chars = roman_string[j] + roman_string[j + 1]
        if chars in subs:
            num += subs[chars]
    return num
