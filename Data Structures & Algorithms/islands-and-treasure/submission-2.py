from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Put all treasure cells into the queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == INF
                ):
                    # First time reaching this land cell:
                    # its shortest distance is current + 1
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))