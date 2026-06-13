from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        elapsed_min = 0
        time = {}  # (row, col) -> minute it became rotten

        fresh = False

        # Initialize queue and time
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh = True
                elif grid[row][col] == 2:
                    queue.append((row, col))
                    time[(row, col)] = 0

        if not fresh:
            return 0

        while queue:
            prow, pcol = queue.popleft()

            for dr, dc in directions:
                nr, nc = prow + dr, pcol + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2          # mark as rotten
                    time[(nr, nc)] = time[(prow, pcol)] + 1
                    elapsed_min = max(elapsed_min, time[(nr, nc)])
                    queue.append((nr, nc))

        # Check if any fresh orange remains
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return elapsed_min