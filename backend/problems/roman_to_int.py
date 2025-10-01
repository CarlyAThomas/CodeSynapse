"""
Problem: Roman to Integer
Difficulty: Easy
Concepts: Hash Maps, Strings
Link: https://leetcode.com/problems/roman-to-integer/
Notes:
- Goal: convert a Roman numeral to an integer
- Key insight: use a hash table to map Roman numerals to integers
- Implementation details: iterate through the string, and for each character, check if the next character is larger (indicating a subtraction)
- Alternate approaches: use a regular expression to match and replace patterns, but this can be less efficient
"""

def roman_to_int(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

def roman_to_int_v2(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev = 0
    
    for char in s:
        curr = roman_map[char]
        if curr > prev:
            total += curr - 2 * prev
        else:
            total += curr
        prev = curr
    return total

def roman_to_int_v3(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')
    total = 0
    for c in s:
        total += roman_map[c]
    return total


# Example usage:
# print(roman_to_int("III"))  # Output: 3
# print(roman_to_int("LVIII"))  # Output: 58
# print(roman_to_int("MCMXCIV"))  # Output: 1994

# print(roman_to_int_v2("III"))  # Output: 3
# print(roman_to_int_v2("LVIII"))  # Output: 58
# print(roman_to_int_v2("MCMXCIV"))  # Output: 1994

# print(roman_to_int_v3("III"))  # Output: 3
# print(roman_to_int_v3("LVIII"))  # Output: 58
# print(roman_to_int_v3("MCMXCIV"))  # Output: 1994