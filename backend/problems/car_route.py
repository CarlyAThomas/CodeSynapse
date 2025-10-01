"""
Problem: Car Route
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: determine the number of days required for a car to cover a given distance
- Key insight: The number of days is the total distance divided by the distance covered per day, rounded up.
- Alternate approaches: Simulate the daily travel until the destination is reached.
"""
"""
A car can cover a distance of N kilometers per day. 
How many days will it take to cover a route of length M kilometers? 
The program gets two numbers: N and M.
"""
def car_route(N, M):
    days = M // N
    if M % N != 0:
        days += 1
    return days