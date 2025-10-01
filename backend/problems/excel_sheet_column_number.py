"""
Problem: Excel Sheet Column Number
Difficulty: Easy
Concepts: Math, Strings
Link: https://leetcode.com/problems/excel-sheet-column-number/
Notes:
- Goal: convert a column title (e.g., "A", "AB") to its corresponding column number (e.g., 1, 28)
- Key insight: use base-26 conversion (like base-10 but with letters)
- Alternate approaches: iterative calculation, memoization
"""
def title_to_number(s):
    result = 0
    for i, char in enumerate(s):
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result