class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # O ( N * N LOG N)
        n = len(grid)
        visit = set()
        min_heap = [[grid[0][0], 0, 0]] # (Time/Max_height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if row == n - 1 and col == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit):
                    visit.add((nr, nc))
                    heapq.heappush(min_heap, [max(time, grid[nr][nc]), nr, nc])
        