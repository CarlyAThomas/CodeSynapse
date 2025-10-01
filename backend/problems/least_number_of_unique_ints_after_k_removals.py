"""
Problem: Least Number of Unique Integers After K Removals
Difficulty: Medium
Concepts: Arrays, Hash Maps, Greedy Algorithms
Link: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
Notes:
- Goal: find the least number of unique integers after removing k elements
- Key insight: use a frequency map to count occurrences and a min-heap to remove the least frequent elements
- Alternate approaches: sorting the array, using a counter
- Instructions: Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
"""
def find_least_num_of_unique_ints(arr, k):
    from collections import Counter
    import heapq

    # Count the frequency of each integer in the array
    freq = Counter(arr)
    
    # Create a min-heap based on the frequency of integers
    min_heap = list(freq.values())
    heapq.heapify(min_heap)
    
    # Remove k elements by removing the least frequent integers first
    while k > 0 and min_heap:
        least_freq = heapq.heappop(min_heap)
        if k >= least_freq:
            k -= least_freq
        else:
            # If we can't remove all occurrences of this integer, push it back with reduced frequency
            heapq.heappush(min_heap, least_freq - k)
            k = 0
    
    # The remaining elements in the heap represent the unique integers left
    return len(min_heap)

def find_least_num_of_unique_ints_sorting(arr, k):
    from collections import Counter

    # Count the frequency of each integer in the array
    freq = Counter(arr)
    
    # Sort the frequencies in ascending order
    sorted_freq = sorted(freq.values())
    
    # Remove k elements by removing the least frequent integers first
    for count in sorted_freq:
        if k >= count:
            k -= count
        else:
            break
    
    
    # The number of unique integers left is the total unique integers minus those we could fully remove
    return len(sorted_freq) - (len(sorted_freq) - sorted_freq.index(count) if k < count else len(sorted_freq))