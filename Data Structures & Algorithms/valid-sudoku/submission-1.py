from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets instead of lists for O(1) lookups
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {i: set() for i in range(9)}

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                
                # Skip empty cells
                if num == '.':
                    continue
                
                # Calculate box index (0 to 8)
                box_i = (row // 3) * 3 + (col // 3)

                # --- The Inline Duplicate Check ---
                if (num in rows[row] or 
                    num in cols[col] or 
                    num in boxes[box_i]):
                    return False  # Found a duplicate! Invalid Sudoku.

                # If it's unique so far, add it to our sets
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_i].add(num)

        return True  # Scanned everything safely, it's valid!