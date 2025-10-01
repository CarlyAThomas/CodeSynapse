"""
Problem: Previous and Next
Difficulty: Easy
Concepts: Arrays, Two Pointers
Link: https://leetcode.com/problems/previous-and-next/
Notes:
- Goal: find previous and next elements in an array based on parity
- Key insight: use two-pointer technique to efficiently locate elements
- Alternate approaches: linear scan, binary search
"""
def find_previous_and_next(arr, target):
    prev = None
    next = None
    for i in range(len(arr)):
        if arr[i] == target:
            if i > 0:
                prev = arr[i - 1]
            if i < len(arr) - 1:
                next = arr[i + 1]
            break
    return prev, next