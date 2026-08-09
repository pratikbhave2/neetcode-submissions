class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        def backtrack(i, curr):
            output.append(curr[::])


            # Include nums[i]
            for start in range(i, n):
                curr.append(nums[start])
                backtrack(start + 1, curr)
                curr.pop()
            
            # Exclude nums[i]
            # backtrack(i+ 1, curr)
        backtrack(0, [])

        return output
