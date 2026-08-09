class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## BFS: TIME COMPLEXITY: ( O ( m * n))
        # ROWS, COLS = len(heights), len(heights[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # pac = [[False] * COLS for _ in range(ROWS)]
        # atl = [[False] * COLS for _ in range(ROWS)]

        # def bfs(source, ocean):
        #     q = deque(source)
        #     while q:
        #         r, c = q.popleft()
        #         ocean[r][c] = True

        #         for dr, dc in directions:
        #             nr, nc = dr + r, dc + c
        #             if ((0 <= nr < ROWS) and (0 <= nc < COLS) and not ocean[nr][nc] and (heights[nr][nc] >= heights[r][c])):
        #                 q.append((nr, nc))

        
        # pacific = []
        # atlantic = []

        # for c in range(COLS):
        #     pacific.append((0, c))
        #     atlantic.append((ROWS - 1, c))

        # for r in range(ROWS):
        #     pacific.append((r, 0))
        #     atlantic.append((r, COLS - 1))
        
        # bfs(pacific, pac)
        # bfs(atlantic, atl)

        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if pac[r][c] and atl[r][c]:
        #             res.append((r, c))

        # return res

        ## DFS

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                dfs(row, col, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))

        return res