"""
Problem: Two Letter to Number
Difficulty: Easy
Concepts: Math
Link:
Notes:
- Goal: Write a program that takes two upper case letters as input and prints its position number 
  in alphabet sequence, [A, B, C, .... X, Y, Z, AA, AB, AC, AD .... AX, AY, AZ, ... ZX, ZY, ZZ]
- Key insight: Use the ASCII value of the characters to determine their positions.
- Alternate approaches: None
"""

def two_letter_to_number(s):
    result = 0
    for char in s:
        value = ord(char) - 64  # 'A' is 65 in ASCII
        result = result * 26 + value
    return result