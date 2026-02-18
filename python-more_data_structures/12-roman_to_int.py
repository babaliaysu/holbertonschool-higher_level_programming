#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roma_reqemleri = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    cem = 0
    ln = len(roman_string)

    for i in range(ln):
        deyer = roma_reqemleri.get(roman_string[i], 0)
        if i + 1 < ln and deyer < roma_reqemleri.get(roman_string[i + 1], 0):
            cem -= deyer
        else:
            cem += deyer

    return cem
