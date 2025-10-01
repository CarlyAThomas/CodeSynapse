"""
Problem: Letter to Number
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: Write a program that takes a single upper case letter as input and prints its position number in alphabet sequence.
- Key insight: Use the ASCII value of the character to determine its position. https://www.asciitable.com/
  Key parts to remember from the table: 'A' = 65, 'Z' = 90 'a' = 97, 'z' = 122 '0' = 48, '9' = 57
- Alternate approaches: None
"""
def letter_to_number(letter):
    return ord(letter) - ord('A') + 1

def letter_to_number_v2(letter):
    return ord(letter) - 64