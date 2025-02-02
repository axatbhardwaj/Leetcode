def romanToInt(s: str) -> int:
    roman_map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" :1000
    }

    number = 0 

    for i in range(len(s)) :
        if (i < len(s)-1) :
            if roman_map[s[i]] < roman_map[s[i+1]] :
                number += (roman_map[s[i+1]] - roman_map[s[i]])
                i += 1
            else :
                number += roman_map[s[i]]
        else :
            number += roman_map[s[i]]

    print(number)
    return number

romanToInt("III")


def romanToInt(s: str) -> int:
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            number += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            number += roman_map[s[i]]
            i += 1

    print(number)
    return number

romanToInt("LIX")