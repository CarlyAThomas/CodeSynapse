"""
Problem: Remove Duplicates from Sorted Array
Difficulty: Easy
Concepts: Arrays, Two Pointers
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Notes:
- Goal: remove duplicates in-place from a sorted array
- Key insight: use two pointers to track unique elements
- Alternate approaches: using a set (but not in-place)
"""
def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index