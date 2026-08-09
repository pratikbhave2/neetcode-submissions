class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visit = set()

        # Multi source BFS so we need to add all of them in the first place in teh qqueue
        q = deque()

        # Add every treasure as a BFS starting point
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] !=  2147483647):
                    continue

                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))