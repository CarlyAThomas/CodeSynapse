"""
Problem: Longest Common Prefix
Difficulty: Easy
Concepts: Strings, Sorting
Link: https://leetcode.com/problems/longest-common-prefix/
Notes:
- Goal: Find the longest common prefix string amongst an array of strings.
- Key insight: If we sort the array, the longest common prefix must be between the first and last strings.
- Alternate approaches: Vertical scanning, Divide and conquer.
"""
# Best approach
# O(S) time complexity, where S is the sum of all characters in all strings
# O(1) space complexity
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sort the array
    strs.sort()
    
    # Compare the first and last strings
    first, last = strs[0], strs[-1]
    i = 0
    
    # Find the common prefix length
    while i < min(len(first), len(last)) and first[i] == last[i]:
        i += 1
    
    return first[:i]

def longest_common_prefix_alt(strs):
    if not strs:
        return ""
    
    pref = ""
    r = max(len(s) for s in strs)
    while len(pref) < r:
        c = None
        for s in strs:
            if len(s) == len(pref):
                return pref
            if c is None:
                c = s[len(pref)]
            elif s[len(pref)] != c:
                return pref
        pref += c
    return pref
