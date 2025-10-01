"""
Problem: School Desks
Difficulty: Easy
Concepts: Math, Simulation
Link: https://leetcode.com/problems/
Notes:
- Goal: calculate the minimum number of desks needed for three classes
- Key insight: Each desk can seat two students, so the number of desks needed is half the number of students, rounded up.
- Alternate approaches: Simulate the seating arrangement.
"""

"""A school decided to replace the desks in three classrooms. Each desk sits two students. 
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
For example, in the first test there are three groups. 
The first group has 20 students and thus needs 10 desks. 
The second group has 21 students, so they can get by with no fewer than 11 desks. 
11 desks is also enough for the third group of 22 students. So we need 32 desks in total.
"""
def school_desks(a, b, c):
    desks_a = (a + 1) // 2
    desks_b = (b + 1) // 2
    desks_c = (c + 1) // 2
    total_desks = desks_a + desks_b + desks_c
    print(total_desks)