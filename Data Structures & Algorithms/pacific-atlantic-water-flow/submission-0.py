from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        
        # 1. Initialize queues for multisource BFS
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Track visited/reachable cells
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # 2. Load up the boundary points
        for r in range(ROWS):
            pacific_queue.append((r, 0))
            pacific_reachable.add((r, 0))
            
            atlantic_queue.append((r, COLS - 1))
            atlantic_reachable.add((r, COLS - 1))
            
        for c in range(COLS):
            pacific_queue.append((0, c))
            pacific_reachable.add((0, c))
            
            atlantic_queue.append((ROWS - 1, c))
            atlantic_reachable.add((ROWS - 1, c))
            
        # 3. Helper function to run the multisource BFS
        def bfs(queue, reachable_set):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Out of bounds check
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        # Already visited check
                        if (nr, nc) not in reachable_set:
                            # UPHILL check (Equal or higher)
                            if heights[nr][nc] >= heights[r][c]:
                                reachable_set.add((nr, nc))
                                queue.append((nr, nc))
                                
        # 4. Run BFS for both oceans simultaneously
        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)
        
        # 5. Return intersection where both 'ticked' the points
        return [list(cell) for cell in (pacific_reachable & atlantic_reachable)]