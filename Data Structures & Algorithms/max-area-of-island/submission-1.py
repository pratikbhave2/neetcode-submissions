class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # # DFS
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
   
        # Directions for movement: up, down, left, right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or(r, c) in visit):
                        continue

                    q.append((nr, nc))
                    visit.add((nr, nc))
                    area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    # Calculate the area of the island starting from this cell
                    max_area = max(max_area, bfs(r, c))

        return max_area