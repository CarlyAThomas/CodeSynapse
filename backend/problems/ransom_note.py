"""
Problem: Ransom Note 
Difficulty: Easy
Concepts: Hash Maps, Strings
Link: https://leetcode.com/problems/ransom-note/
Notes:
- Goal: Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
  from magazine and false otherwise.
- Key insight: Use a frequency counter to track character counts.
  Counter collects letters if you pass a string, and counts words if you pass a list of strings.
  It counts the frequency of each element and stores it in a dictionary-like structure 
  so technically you can pass it anything that is iterable such as a string, list, or tuple.
- Alternate approaches: Sort both strings and compare.
"""
def can_construct(ransom_note, magazine):
    from collections import Counter
    ransom_count = Counter(ransom_note)
    magazine_count = Counter(magazine)
    
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True