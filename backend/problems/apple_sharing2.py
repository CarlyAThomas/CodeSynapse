"""
Problem: Apple Sharing 2
Difficulty: Easy
Concepts: Counting, Math, Modulus
Link: https://leetcode.com/problems/apple-sharing/
Notes:
- Goal: distribute apples among friends such that each friend gets the same number of apples
- Key insight: use integer division and modulus to determine distribution and remainder
- Alternate approaches: greedy algorithm, binary search
"""

def distribute_apples(N, K):
    apples_per_student = K // N
    remaining_apples = K % N
    return apples_per_student, remaining_apples