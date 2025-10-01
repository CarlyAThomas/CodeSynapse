"""
Problem: Sort Array By Parity
Difficulty: Easy
Concepts: Arrays, Two Pointers
Link: https://leetcode.com/problems/sort-array-by-parity/
Notes:
- Goal: rearrange the array so that all even integers come before all odd integers
- Key insight: use two pointers to partition the array
- Alternate approaches: using a stable sort
"""
def sort_array_by_parity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 == 1:
            right -= 1
    return nums