class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        # area = 0
        # directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
        # ROWS = len(grid)
        # COLS = len(grid[0])
        # visit = set()

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= ROWS or c >=COLS or grid[r][c] == 0 or (r,c) in visit):
        #         return 0
            
        #     visit.add((r,c))
        #     count = 1
        #     for dr, dc in directions:
        #         count += dfs(dr + r, dc + c)
        #     return count


        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1 and (r,c) not in visit:
        #             area = max(area, dfs(r, c))


        # return area


        area = 0
        directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()


        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            count = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >=COLS or grid[nr][nc] ==0 or (nr, nc) in visit):
                        continue

                    count += bfs(nr, nc)
                    visit.add((nr, nc))
                    q.append((nr, nc))


            return count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area, bfs(r, c))


        return area
        
