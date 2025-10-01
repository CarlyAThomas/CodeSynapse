"""
Problem: Swap Last Two Digits
Difficulty: Easy
Concepts: Math, Modulus
Link:
Notes:
- Goal: Given an integer greater than 9, print a new number that has the two digits in the reverse order, 1's value first, and then 10's value.
- Key insight: Use modulus and integer division to extract and swap the last two digits.
- Alternate approaches: String conversion to manipulate digits.
"""
def swap_last_two_digits(n):
    if n < 10:
        print("Invalid input")
        return
    ones = n % 10
    tens = (n // 10) % 10
    new_number = ones * 10 + tens
    print(new_number)