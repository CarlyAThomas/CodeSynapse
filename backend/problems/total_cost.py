"""
Problem: Total Cost
Difficulty: Easy
Concepts: Math
Link:
Notes:
- Goal: Calculate the total cost of N cupcakes given the cost of one cupcake in dollars and cents.
- Key insight: Convert the cost of one cupcake to cents, multiply by N, and then convert back to dollars and cents.
- Alternate approaches: Use a single variable to keep track of total cents instead of separate dollar and cent variables.
"""

def total_cost(A, B, N):
    total_cents = (A * 100 + B) * N
    total_dollars = total_cents // 100
    remaining_cents = total_cents % 100
    return total_dollars, remaining_cents