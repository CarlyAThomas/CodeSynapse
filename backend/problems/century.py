"""
Problem: Century
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: Given a year (as a positive integer), find the respective number of the century. 
  Note that, for example, 20th century began with the year 1901.
- Key insight: Use integer division and modulus to determine the century.
- Alternate approaches: None
"""
"""
Given a year (as a positive integer), find the respective number of the century. 
Note that, for example, 20th century began with the year 1901.
"""
def find_century(year):
    if year % 100 == 0:
        return year // 100
    return year // 100 + 1