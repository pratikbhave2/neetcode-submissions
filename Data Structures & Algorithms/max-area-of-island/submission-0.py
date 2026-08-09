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
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()
        # max_area = 0

        # def dfs(r, c):
        #     # Base case: If out of bounds, water, or already visited, return 0
        #     if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visit):
        #         return 0
        #     # Mark the cell as visited
        #     visit.add((r, c))
        #     # Initialize area of the current cell
        #     area = 1
        #     # Explore all 4 directions
        #     for dr, dc in directions:
        #         area += dfs(r + dr, c + dc)
        #     return area

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r, c) not in visit:
        #             # Calculate the area of the island starting from this cell
        #             max_area = max(max_area, dfs(r, c))

        # return max_area