"""
Problem: Swap Two Digits
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: Swap the digits of a two-digit integer and print the result.
- Key insight: Use integer division and modulus to extract digits.
- Alternate approaches: String conversion.
"""
def swap_two_digits(n):
    tens_digit = n // 10
    ones_digit = n % 10
    swapped_number = ones_digit * 10 + tens_digit
    return swapped_number