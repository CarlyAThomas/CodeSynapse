"""
Problem: Length of Last Word
Difficulty: Easy
Concepts: Strings
Link: https://leetcode.com/problems/length-of-last-word/
Notes:
- Goal: find the length of the last word in a string
- Key insight: use string manipulation to isolate the last word
- Idea: You would go to the end of the string and move backwards until you find a non-space character, 
  then continue moving backwards until you find a space or the beginning of the string, counting the characters in between.
- Alternate approaches: regular expressions, split and trim
- Instructions: Given a string s consisting of words and spaces, return the length of the last word.
"""
def length_of_last_word(s):
    # Strip trailing spaces and split the string into words
    words = s.strip().split()
    # Return the length of the last word, or 0 if there are no words
    return len(words[-1]) if words else 0

def length_of_last_word_alternate(s):
    # Initialize length counter
    length = 0
    # Start from the end of the string and move backwards
    i = len(s) - 1
    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
    # Count the length of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length

def length_of_last_word_alternate_2(s):
    # Using rfind to locate the last space and calculate length
    count = 0
    for i in reversed(range(len(s))):
        if s[i] != ' ':
            count += 1
        elif count > 0:
            break
    return count