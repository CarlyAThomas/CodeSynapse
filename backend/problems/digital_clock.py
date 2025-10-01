"""
Problem: Digital Clock
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: Convert minutes since midnight to hours and minutes.
- Key insight: Use integer division and modulo to find hours and minutes.
- Alternate approaches: Precompute all possible times.
"""
def digital_clock(N):
    hours = (N // 60) % 24
    minutes = N % 60
    return hours, minutes