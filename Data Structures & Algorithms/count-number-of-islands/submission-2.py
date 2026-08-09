class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visit = set()
        islands = 0

        def dfs(r, c):
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >=COLS or (nr, nc) in visit or grid[nr][nc] == "0":
                    continue
                
                visit.add((nr, nc))
                dfs(nr, nc)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands
