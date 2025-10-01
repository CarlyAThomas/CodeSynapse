"""
Problem: Digit After Decimal Point
Difficulty: Easy
Concepts: Math, Strings
Link: https://leetcode.com/problems/digit-after-decimal-point/
Notes:
- Goal: Find the digit after the decimal point of a given float.
- Key insight: Use modulus and integer division to isolate the digit.
- Alternate approaches: Convert the float to a string and access the digit directly.
"""
def digit_after_decimal(n):
    # Isolate the digit after the decimal point
    return int((n * 10) % 10)