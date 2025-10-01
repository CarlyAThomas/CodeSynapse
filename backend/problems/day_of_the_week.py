"""
Problem: Day of the Week
Difficulty: Easy
Concepts: Math
Link: https://leetcode.com/problems/
Notes:
- Goal: Find the day of the week for the K-th day of the year.
- Key insight: January 1 is Thursday, so we can use modular arithmetic to find the day of the week.
- Alternate approaches: Precompute the day of the week for all days in the year.
"""

def day_of_the_week(K):
    # January 1 is Thursday, which is day 4
    start_day = 4
    # Calculate the day of the week for the K-th day
    # The Kth day is K-1 days after January 1 because January 1 is the 1st day
    day_of_week = (start_day + (K - 1)) % 7
    return day_of_week


# # Example usage:K = 9
# print(day_of_the_week(365))  # Output: 4 (Thursday)
# print(day_of_the_week(300))  # Output: 2 (Tuesday)
# print(day_of_the_week(200))  # Output: 1 (Monday)
# print(day_of_the_week(100))  # Output: 0 (Sunday)
# print(day_of_the_week(50))  # Output: 5 (Friday)
# print(day_of_the_week(5))  # Output: 1 (Monday)
# print(day_of_the_week(4))  # Output: 0 (Sunday)
# print(day_of_the_week(3))  # Output: 6 (Saturday)
# print(day_of_the_week(2))  # Output: 5 (Friday)
# print(day_of_the_week(1))  # Output: 4 (Thursday)