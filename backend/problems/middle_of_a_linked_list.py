"""
Problem: Middle of a Linked List
Difficulty: Easy
Concepts: Linked Lists, Two Pointers
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Notes:
- Goal: Given the head of a singly linked list, return the middle node of the linked list.
  If there are two middle nodes, return the second middle node.
- Key insight: Use slow/fast pointer to find middle.
- Alternate approaches: Count nodes, then find middle.  
"""
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
