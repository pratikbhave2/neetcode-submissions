class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion
        # o ( 2 ^ n)

        # def dfs(i):
        #     if i >=n:
        #         return i == n
        #     return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)


        # Dynamic Programming (Top-Down)
        # O(n)
        cache = [None] * n

        def dfs(i):
            if i >= n:
                return i == n

            if cache[i] != None:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)