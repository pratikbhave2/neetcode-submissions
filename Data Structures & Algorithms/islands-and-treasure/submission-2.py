class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        MAX_INT = (2 ** 31) - 1
        # (Up, Right, Down, Left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        q = deque()
        # Find all the treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        
        # do bfs

        while q:
            length = len(q)
            for i in range(length):
                r, c, level = q.popleft()
                grid[r][c] = level
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == MAX_INT:
                        grid[nr][nc] = level + 1
                        q.append((nr, nc, level + 1))
        
        

        

