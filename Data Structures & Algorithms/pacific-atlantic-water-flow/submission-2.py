class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # # BFS(O (M * N)) space
        # # O (m * n) time

        # ROWS = len(heights)
        # COLS = len(heights[0])
        # # Directions: Up - > Right -> Down -> Left
        # directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # # to keep tab of water flowing into the pacific and atlantic individually
        # pac_waterflow = [[False for i in range (COLS)] for _ in range(ROWS)]
        # atl_waterflow = [[False for i in range (COLS)] for _ in range(ROWS)]

        # # Mark the border columns/rows for atlantic and pacific water flow
        # pacific_visited = []
        # atlantic_visited = []
        # for c in range(COLS):
        #     pacific_visited.append((0, c)) # first row, all columns
        #     atlantic_visited.append(((ROWS - 1), c)) # Last row, all columns

        # for r in range(ROWS):
        #     pacific_visited.append((r, 0)) # first col, all rows
        #     atlantic_visited.append((r, (COLS - 1))) # Last col, all rows

        # def bfs(source_visited, ocean_waterflow):
        #     q = deque(source_visited)
        #     while q:
        #         row, col = q.popleft()
        #         ocean_waterflow[row][col] = True
        #         # BFS in all 4 directions
        #         for dr, dc in directions:
        #             nr, nc = dr + row, dc + col
        #             if 0 <= nr < ROWS and 0 <= nc < COLS and not ocean_waterflow[nr][nc] and heights[nr][nc] >= heights[row][col]:
        #             # if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or ocean_waterflow[nr][nc] or heights[row][col] > heights[nr][nc]:
        #             #     continue
        #                 q.append((nr, nc))

        # bfs(pacific_visited, pac_waterflow)
        # bfs(atlantic_visited, atl_waterflow)

        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if pac_waterflow[r][c] and atl_waterflow[r][c]:
        #             res.append((r, c))
        # return res


        # DFS(O (M * N)) space
        # O (m * n) time

        ROWS = len(heights)
        COLS = len(heights[0])
        # Directions: Up - > Right -> Down -> Left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # to keep tab of water flowing into the pacific and atlantic individually
        pac = set()
        atl = set()


        def dfs(row, col, source_visited, prev_height):
            if (row, col) in source_visited or row < 0 or row >= ROWS or col < 0 or col >= COLS or heights[row][col] < prev_height:
                return
            
            source_visited.add((row, col))
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                dfs(nr, nc, source_visited, heights[row][col])

        # Call dfs on border columns/rows for atlantic and pacific water flow
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




