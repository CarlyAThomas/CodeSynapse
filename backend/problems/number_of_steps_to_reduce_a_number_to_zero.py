"""
Problem: Number of Steps to Reduce a Number to Zero
Difficulty: Easy
Concepts: Math, Simulation
Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Notes:
- Goal: Given an integer num, return the number of steps to reduce it to zero.
  In one step, if the current number is even, you have to divide it by 2, 
  otherwise, you have to subtract 1 from it.
- Key insight: If the number is even, divide it by 2. If it's odd, subtract 1.
- Alternate approaches: We could also use a loop to repeatedly apply these operations until the number reaches zero.
"""
def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps