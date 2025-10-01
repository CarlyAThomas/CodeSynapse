"""
Problem: Clock Face
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: Find the angle turned by the minute hand since the start of the current hour.
- Key insight: The minute hand moves 6 degrees for each minute (360 degrees / 60 minutes).
- Alternate approaches: Precompute the angles for each minute.
"""
def minute_hand_angle(alpha):
    minutes = (alpha % 360) * 2  # Each hour (30 degrees) corresponds to 60 minutes, so each degree corresponds to 2 minutes
    return (minutes % 60) * 6  # Each minute corresponds to 6 degrees