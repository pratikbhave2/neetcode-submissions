class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Solve using DFS
        # THis is terrieebly slow (O (m * n * 4 ^ (m * n)))
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647
        # visit = [[False for _ in range(COLS)] for _ in range(ROWS)]

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= ROWS or
        #         c >= COLS or grid[r][c] == -1 or
        #         visit[r][c]):
        #         return INF
        #     if grid[r][c] == 0:
        #         return 0

        #     visit[r][c] = True
        #     res = INF
        #     for dx, dy in directions:
        #         res = min(res, 1 + dfs(r + dx, c + dy))
        #     visit[r][c] = False
        #     return res

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == INF:
        #             grid[r][c] = dfs(r, c)


        ## Solve using BFS
        # DO BFS From the gates instead of rooms simultaneously from all gates
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


