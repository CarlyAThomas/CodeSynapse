"""
Problem: Sum of Digits
Difficulty: Easy
Concepts: Math, Loops
Link: https://leetcode.com/problems/sum-of-digits/
Notes:
- Goal: Find the sum of the digits of a given integer without using string operations.
- Key insight: Use a loop to extract and sum each digit.
- Alternate approaches: Convert the number to a string and sum the digits directly.
"""
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total