class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i, curr, curr_sum):
            if i >=n:
                return

            if curr_sum == target:
                res.append(curr[:])
                return

            if curr_sum > target:
                return

            backtrack(i + 1, curr, curr_sum)
            curr.append(nums[i])
            backtrack(i, curr, curr_sum + nums[i])
            curr.pop()
        
        backtrack(0, [], 0)
        return res