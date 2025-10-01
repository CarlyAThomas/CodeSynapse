"""
Problem: Count Number of Bits in Position
Difficulty: Easy
Concepts: Bit Manipulation
Link: https://leetcode.com/problems/
Notes:
- Goal: Given five input numbers, a, b, c, d and n, print out the number of 1 bits at the 
  nth least significant bit position in all four numbers a, b, c, d.
  Note: The positions are 0-indexed from the right.
- Key insight: The bitwise AND operator `&` can be used to isolate the nth bit of a number. 
  For example, `x & (1 << n)` will be non-zero if the nth bit of `x` is 1.
- Alternate approaches: None
"""
def count_bits_in_position(a, b, c, d, n):
    count = 0
    for number in [a, b, c, d]:
        if number & (1 << n): # Check if the nth bit is set
            count += 1
    print(count)
    
# Example usage:
# count_bits_in_position(2, 3, 5, 6, 1)  # Output: 3
# Explanation:
# 2 in binary is 10 (1 at position 1)
# 3 in binary is 11 (1 at position 1)
# 5 in binary is 101 (0 at position 1)
# 6 in binary is 110 (1 at position 1)
# So, there are three 1s at position 1.
# Positions are 0-indexed from the right.
# count_bits_in_position(5, 3, 7, 10, 1)  # Output: 3
# count_bits_in_position(8, 9, 10, 11, 3)   # Output: 4
# count_bits_in_position(15, 15, 15, 15, 3) # Output: 4
# count_bits_in_position(0, 0, 0, 0, 2)    # Output: 0