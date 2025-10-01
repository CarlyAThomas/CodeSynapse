"""
Problem: Apple Sharing
Difficulty: Easy
Concepts: Counting, Arrays, Hash Maps
Link: https://leetcode.com/problems/apple-sharing/
Notes:
- Goal: distribute apples among friends such that each friend gets the same number of apples
- Key insight: use counting to determine the minimum number of moves
- Alternate approaches: greedy algorithm, binary search
"""
def min_moves_to_share_apples(apples, k):
    from collections import Counter
    count = Counter(apples)
    total_moves = 0
    for num_apples, freq in count.items():
        if num_apples < k:
            total_moves += freq * (k - num_apples)
    return total_moves

# # Example usage:
# apples = [1, 2, 3, 4, 5]
# k = 3
# print(min_moves_to_share_apples(apples, k))  # Output: 6