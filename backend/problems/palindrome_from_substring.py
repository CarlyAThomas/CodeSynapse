"""
Problem: Make Palindrome from Substring
Difficulty: Easy
Concepts: Arrays, Two Pointers, Strings
Link: https://leetcode.com/problems/make-palindrome-from-substring/
Notes:
- Goal: determine if a substring can be rearranged to form a palindrome
- Key insight: use character frequency to check for palindrome possibility
- Alternate approaches: backtracking, dynamic programming
"""
def can_make_palindrome(s):
    from collections import Counter
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_count <= 1