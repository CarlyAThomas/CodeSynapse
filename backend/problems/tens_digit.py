"""
Problem: Tens Digit
Difficulty: Easy
Concepts: Math, Modulus
Link: https://leetcode.com/problems/tens-digit/
Notes:
- Goal: Find the tens digit of a given integer.
- Key insight: Use integer division and modulus to isolate the tens digit.
- Alternate approaches: Convert the number to a string and access the tens digit directly.
"""
def tens_digit(n):
    if n < 10:
        return 0  # No tens digit
    return (n // 10) % 10