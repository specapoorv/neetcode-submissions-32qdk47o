class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,-1), (-1,0), (0, 1), (1,0)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col):
            grid[row][col] = 0
            for dr,dc in directions:
                nr,nc = dr+row, dc+col
                if (
                    0<=nr<rows and 0<=nc<cols and
                    grid[nr][nc] == '1'
                ):
                    dfs(nr, nc)
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count


            
            








        