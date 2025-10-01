"""
Problem: Area of a Triangle
Difficulty: Easy
Concepts: Math, Geometry
Link: https://leetcode.com/problems/area-of-a-triangle/
Notes:
- Goal: calculate the area of a triangle given its vertices
- Key insight: use the determinant formula for area calculation
- Alternate approaches: Heron's formula, vector cross product
"""
def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)