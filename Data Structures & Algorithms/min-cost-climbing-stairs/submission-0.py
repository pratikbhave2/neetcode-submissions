class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion
        # o 2^n
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
            
        #     return cost[i] + min(dfs(i + 1) + dfs(i + 2))
        
        # return min(dfs(0), dfs(1))


        # # DP Bottom up
        # # O(n)
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i - 2] + cost[i - 2])

        return dp[n]
