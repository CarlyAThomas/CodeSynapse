"""
Problem: Two Bits
Difficulty: Easy
Concepts: Bit Manipulation
Link: https://leetcode.com/problems/swap-two-bits/
Notes:
- Goal: Print the two bits of a 2-bit integer.
- Key insight: Use integer division and modulus to extract bits.
- Alternate approaches: String conversion.
"""
def print_twos_and_ones(n):
    twos_bit = (n // 2) % 2
    ones_bit = n % 2
    print(twos_bit, ones_bit)