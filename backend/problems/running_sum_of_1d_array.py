"""
Problem: Running Sum of 1d Array
Difficulty: Easy
Concepts: Arrays, Prefix Sum
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Notes:
- Goal: compute the running sum of a 1D array
- Key insight: use a prefix sum array to store cumulative sums
- Alternate approaches: iterative in-place modification
- Instructions: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
"""
def running_sum(nums):
    running_sum_array = []
    current_sum = 0
    for num in nums:
        current_sum += num
        running_sum_array.append(current_sum)
    return running_sum_array