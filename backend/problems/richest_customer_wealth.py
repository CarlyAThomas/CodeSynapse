"""
Problem: Richest Customer Wealth
Difficulty: Easy
Concepts: Arrays, Simulation
Link: https://leetcode.com/problems/richest-customer-wealth/
Notes:
- Goal: You are given an m x n integer grid accounts where accounts[i][j] is the amount of 
  money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

  A customer's wealth is the amount of money they have in all their bank accounts. 
  The richest customer is the customer that has the maximum wealth.
- Key insight: To find the richest customer, we need to calculate the wealth of each customer 
  by summing the amounts in their respective rows (bank accounts) and keep track of the maximum 
  wealth found.
- Alternate approaches: We could also use a priority queue to keep track of the top customers 
  by wealth, but this would be less efficient than a simple linear scan.
"""
def richest_customer_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        current_wealth = sum(customer)
        if current_wealth > max_wealth:
            max_wealth = current_wealth
    return max_wealth