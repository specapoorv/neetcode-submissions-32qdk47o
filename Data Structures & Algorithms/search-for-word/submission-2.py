from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get_choices(row, column):
            top = (row-1, column)
            right = (row, column + 1)
            bottom = (row+1, column)
            left = (row, column-1)

            if row == 0:
                top = None
            elif row == len(board)-1:
                bottom = None
            if column == 0:
                left = None
            elif column == len(board[0]) - 1:
                right = None
            
            return [top, right, bottom, left]

        def backtrack(row, column, path, w_i, visited):
            
            # 🔥 bounds check (needed!)
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
                return False

            # 🔥 visited check
            if (row, column) in visited:
                return False

            # 🔥 match FIRST
            if board[row][column] != word[w_i]:
                return False

            # 🔥 success AFTER match
            if w_i == len(word) - 1:
                return True

            visited.add((row, column))

            for choice in get_choices(row, column):
                if choice is None:
                    continue
                next_row, next_column = choice

                if backtrack(next_row, next_column, path, w_i + 1, visited):
                    return True

            visited.remove((row, column))

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, "", 0, set()):
                    return True

        return False