"""
Problem: Valid Sudoku
Difficulty: Medium
Concepts: Hash Maps, Matrices
Link: https://leetcode.com/problems/valid-sudoku/
Notes:
- Goal: determine if a 9x9 Sudoku board is valid
- Key insight: use a hash map to track seen numbers
- Alternate approaches: backtracking, bit manipulation
"""
def is_valid_sudoku(board):
    rows = [{} for _ in range(9)]
    cols = [{} for _ in range(9)]
    boxes = [{} for _ in range(9)]  # 3x3 boxes

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != '.':
                box_index = (r // 3) * 3 + (c // 3)
                rows[r][num] = rows[r].get(num, 0) + 1
                cols[c][num] = cols[c].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                if rows[r][num] > 1 or cols[c][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True