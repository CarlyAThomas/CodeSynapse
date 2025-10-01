"""
Problem: Two Digits
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/two-digits/
Notes:
- Goal: Print the tens and ones digits of a two-digit integer.
- Key insight: Use integer division and modulus to extract digits.
- Alternate approaches: String conversion.
"""
def print_tens_and_ones(n):
    tens_digit = n // 10
    ones_digit = n % 10
    print(tens_digit, ones_digit)
