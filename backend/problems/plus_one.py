"""
Problem: Plus One
Difficulty: Easy
Concepts: Arrays, Math
Link: https://leetcode.com/problems/plus-one/
Notes:
- Goal: increment a large integer represented as an array of digits
- Key insight: handle carry propagation from the least significant digit
- Alternate approaches: using a string representation
"""
def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits