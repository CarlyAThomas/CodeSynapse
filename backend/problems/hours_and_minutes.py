"""
Problem: Hours and Minutes
Difficulty: Easy
Concepts: Math, Simulation
Link: https://leetcode.com/problems/hours-and-minutes/
Notes:
- Goal: convert time from hours and minutes to total minutes
- Key insight: use simple arithmetic to perform the conversion
- Alternate approaches: string manipulation, built-in functions
"""
def convert_to_minutes(hours, minutes):
    return hours * 60 + minutes