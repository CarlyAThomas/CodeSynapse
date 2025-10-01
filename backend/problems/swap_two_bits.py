"""
Problem: Swap Two Bits
Difficulty: Easy
Concepts: Bit Manipulation
Link: https://leetcode.com/problems/swap-two-bits/
Notes:
- Goal: Swap the last two bits of a 2-bit integer.
- Key insight: Use bit manipulation to isolate and swap bits.
- Alternate approaches: String conversion.
"""

def print_last_two_bits(n):
    ones_bit = n % 2
    twos_bit = (n // 2) % 2
    print(ones_bit, twos_bit)
