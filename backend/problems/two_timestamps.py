"""
Problem: Two Timestamps
Difficulty: Easy
Concepts: Arrays, Counting, Hash Maps
Link: https://leetcode.com/problems/two-timestamps/
Notes:
- Goal: find the difference between two timestamps
- Key insight: convert timestamps to minutes and calculate the difference
- Alternate approaches: string manipulation, built-in functions
"""
def find_timestamp_difference(t1, t2):
    def to_minutes(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    minutes1 = to_minutes(t1)
    minutes2 = to_minutes(t2)
    return abs(minutes1 - minutes2)