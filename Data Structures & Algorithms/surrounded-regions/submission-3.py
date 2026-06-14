class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        queue = deque()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if (row == 0
                    or col == 0
                    or row == rows-1
                    or col == cols-1):
                        if board[row][col] == 'O':
                            queue.append((row,col))
                            visited.add((row,col))
                        
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if (
                    0<=nr<rows-1 and 0<=nc<cols-1
                    and board[nr][nc] == 'O'
                    and (nr,nc) not in visited
                ):
                    visited.add((nr,nc))
                    queue.append((nr,nc))

        for row in range(rows):
            for col in range(cols):
                if (
                    board[row][col] == 'O'
                    and (row,col) not in visited
                ):
                    board[row][col] = 'X'
                    




