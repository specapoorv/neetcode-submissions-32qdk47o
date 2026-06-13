class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0 and grid[row][col] != -1:
                    grid[row][col] = self.bfs(grid, row, col) 


    def bfs(self, grid, row, col):
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([(row,col,0)])
        visited = set([(row, col)])

        while queue:
            prow, pcol, dist = queue.popleft()
            if grid[prow][pcol] == 0:
                return dist
        
            for dir in directions:
                r, c = dir
                nr, nc = prow + r, pcol + c
                if nr >=0 and nr < rows and nc >=0 and nc < cols and grid[nr][nc] != -1:
                    if (nr, nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr, nc, dist+1))


            
                
        
        





        