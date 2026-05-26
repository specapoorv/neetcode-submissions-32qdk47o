class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.max_area = 0

        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == 1:
                    self.area = 1
                    if self.area > self.max_area:
                        self.max_area = self.area
                    self.bfs(grid, r, c)
        
        return self.max_area
        
    
    def bfs(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((r, c))
        grid[r][c] = 0
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if nr > rows-1 or nr < 0 or nc > cols-1 or nc<0:
                    continue
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
                    self.area += 1
                    if self.area>self.max_area:
                        self.max_area = self.area
                
            
            
            
        