"""
Problem: Print Letters from Column
Difficulty: Easy
Concepts: Strings
Link: https://leetcode.com/problems/
Notes:
- Goal: Write a program that takes upper case letters (an Excel Column Number) as input 
  and prints the letters in reverse order.
- Key insight: This is string manipulation only.
- Alternate approaches: None
"""
def print_letters_from_column(column_number):
    return column_number[::-1]

# # Example usage:
# print_letters_from_column("ABCD")  # Output: "DCBA"