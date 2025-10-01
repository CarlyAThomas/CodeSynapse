"""
Problem: Two Sum
Difficulty: Easy
Concepts: Arrays, Hash Maps
Link: https://leetcode.com/problems/two-sum/
Notes:
- Goal: find two numbers that add up to target
- Key insight: use a hash map to store seen numbers
- Alternate approaches: brute force O(n^2), sorting + two pointers O(n log n)
"""
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen= {}
        for i,num in enumerate(nums):
            compliment = target-num
            if compliment in seen:
                return [seen[compliment], i]
            else:
                seen[num] = i
        return []