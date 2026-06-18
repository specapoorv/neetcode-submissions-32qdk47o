class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        adj_list = defaultdict(list)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<len(grid) and 0<=nc<len(grid[0])):
                        adj_list[(row,col)].append((nr,nc))

        n = ROWS*COLS
        peak = [float('inf')]*n
        peak[0] = grid[0][0]

        pq = [(grid[0][0], 0)] #dist, node

        while pq:
            curr_peak, node = heapq.heappop(pq)
            r = node//COLS
            c = node%COLS
            if peak[node] < curr_peak:
                continue
            
            for nr, nc in adj_list[(r,c)]:
                i = (nr*COLS)+nc
                
                max_peak = curr_peak if curr_peak > grid[nr][nc] else grid[nr][nc]

                if max_peak < peak[i]:
                    peak[i] = max_peak
                    heapq.heappush(pq, (max_peak, i))
                
        return peak[-1]