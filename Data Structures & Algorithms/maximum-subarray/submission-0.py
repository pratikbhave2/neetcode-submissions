class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's
        max_sum = float("-inf")
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum

        # brute force
        # O( N * N)
        # n, max_count = len(nums), nums[0]
        # for i in range(n):
        #     count = 0
        #     for j in range(i, n):
        #         count += nums[j]
        #         max_count = max(max_count, count)
        #     # max_count = max(max_count, count)

        # return max_count

