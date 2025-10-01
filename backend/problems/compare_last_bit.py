"""
Problem: Compare Last Bit
Difficulty: Easy
Concepts: Bit Manipulation
Link: https://leetcode.com/problems/
Notes:
- Goal: Given two input numbers, print 'True' if the last least significant bit 
  of the two number match and 'False' if they don't.
- Key insight: Use bitwise AND operation to compare the last bits.
  How bitwise works: The expression `x & 1` isolates the last bit of `x`. 
  If `x` is odd, the last bit is 1; if even, it's 0. Thus, comparing `x & 1` for two numbers 
  tells us if their last bits are the same. If you wanted the second to last bit, you would use `x & 2`,
  for the third to last bit, `x & 4`, and so on.
- Alternate approaches: None
"""
def compare_last_bit(numbers):
    return int(numbers[0])&1 == int(numbers[1])&1

