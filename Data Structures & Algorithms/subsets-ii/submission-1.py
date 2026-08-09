class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []

        def backtrack(i, curr):
            if i == n and curr not in output:
                output.append(curr[:])
                return

            if i == n:
                return
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            backtrack(i + 1, curr)

        backtrack(0, [])
        return output
            