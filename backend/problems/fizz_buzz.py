"""
Problem: Fizz Buzz
Difficulty: Easy
Concepts: Loops, Conditionals
Link: https://leetcode.com/problems/fizz-buzz/
Notes:
- Goal: print numbers 1 to n with FizzBuzz rules
- Key insight: use modulo operator to check divisibility
- Alternate approaches: string concatenation, array mapping
"""

def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result