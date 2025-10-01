"""
Problem: Swap Last Two Digits
Difficulty: Easy
Concepts: Math, Modulus
Link: https://leetcode.com/problems/
Notes:
- Goal: Given an integer greater than 9, print its last two digits in the reverse order, 1's value first, and then 10's value with a space in between.
- Key insight: Use modulus and integer division to extract and swap the last two digits.
- Alternate approaches: String conversion to manipulate digits.
"""
def swap_last_two_digits(n):
    if n < 10:
        print("Invalid input")
        return
    ones = n % 10
    tens = (n // 10) % 10
    print(ones, tens)