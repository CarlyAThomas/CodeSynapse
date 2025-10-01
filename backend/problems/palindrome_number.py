"""
Problem: Palindrome Number
Difficulty: Easy
Concepts: Two Pointers, Strings
Link: https://leetcode.com/problems/palindrome-number/
Notes:
- Goal: determine if an integer is a palindrome
- Key insight: compare characters from both ends towards the center
- Implementation details: use two pointers to check for equality, 
  the while function is < and not <= because the middle character in an odd-length number doesn't need to be checked
- Alternate approaches: convert to string and compare with its reverse, 
  or use mathematical reversal of the number, but be cautious of overflow in some languages
"""

# Two pointers approach Big O(n) time and O(1) space
def is_palindrome(x):
    x = str(x)
    left, right = 0, len(x) - 1
    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

# Alternate approach using string reversal and slicing Big O(n) time and O(n) space
def is_palindrome_alternate(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

# Best approach overall Big O(log10(n)) time and O(1) space
def is_palindrome_best(x):
    # Negative numbers are not palindromes
    # Numbers ending in 0 are not palindromes unless the number is 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    # Reverse the second half of the number
    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10
    # The middle digit doesn't matter in a palindrome but in this case we are adding it to reverted_number
    # We are just going to account for it by doing integer division by 10 in the possible return statement
    # When the length is an odd number, we can get rid of the middle digit by reverted_number // 10
    return x == reverted_number or x == reverted_number // 10

# # Example usage:
# print(is_palindrome("121"))  # True
# print(is_palindrome("-121")) # False
# print(is_palindrome("10"))   # False
# print(is_palindrome("12321")) # True