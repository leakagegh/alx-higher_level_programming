#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }

    n = 0

    for i in range(len(roman_string)):
        if romans.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                romans[roman_string[i]] < romans[roman_string[i + 1]]):
            n += romans[roman_string[i]] * -1
        else:
            n += romans[roman_string[i]]

    return n
