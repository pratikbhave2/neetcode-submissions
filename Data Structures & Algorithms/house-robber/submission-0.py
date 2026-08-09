class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_sum = []
        # Recursion: 2 ^ n
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     return max(dfs(i + 1), nums[i] + dfs(i + 2))
        # return dfs(0)
                
            
            
        # Bottom up DP:
        if not nums:
            return

        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
