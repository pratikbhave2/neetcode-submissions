class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >=COLS or grid[r][c] == 0 or (r,c) in visit):
                return 0
            
            visit.add((r,c))
            count = 1
            for dr, dc in directions:
                count += dfs(dr + r, dc + c)
            return count


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area, dfs(r, c))


        return area