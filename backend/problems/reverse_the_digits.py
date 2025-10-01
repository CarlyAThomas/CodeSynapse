"""
Problem: Reverse the Digits
Difficulty: Easy
Concepts: Math, Modulus, Strings
Link: https://leetcode.com/problems/
Notes:
- Goal: Given an integer greater than 9, print all the digits in the reverse order, 1's value first, and then 10's value and then the 100's value, and so on, with a space in between.
- Key insight: Use modulus and integer division to extract each digit and print them in reverse order.
- Alternate approaches: String conversion to manipulate digits.
"""
def reverse_digits(n):
    if n < 10:
        print("Invalid input")
        return
    reversed_digits = []
    while n > 0:
        reversed_digits.append(n % 10)
        n //= 10
    print(" ".join(map(str, reversed_digits)))