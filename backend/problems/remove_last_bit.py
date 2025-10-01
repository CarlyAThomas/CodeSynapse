"""
Problem: Remove Last Bit
Difficulty: Easy
Concepts: Bit Manipulation
Link: https://leetcode.com/problems/
Notes:
- Goal: Given two input numbers, print out the two numbers with their binary value shifted to the right by 1 bit.
- Key insight: The right shift operator `>>` can be used to shift the bits of a number to the right. 
  For example, `x >> 1` shifts the bits of `x` one position to the right, effectively dividing `x` by 2.
- Alternate approaches: None
"""
def remove_last_bit(numbers):
    return (int(numbers[0]) >> 1, int(numbers[1]) >> 1)
