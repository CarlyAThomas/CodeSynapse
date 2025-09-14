"""
Problem: Valid Palindrome
Difficulty: Easy
Concepts: Two Pointers, Strings
Link: https://leetcode.com/problems/valid-palindrome/
Notes:
- Goal: determine if a string is a palindrome considering only alphanumeric characters and ignoring cases
- Key insight: use two pointers to compare characters
- Alternate approaches: using a stack, reversing the string
"""
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True