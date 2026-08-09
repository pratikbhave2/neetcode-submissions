class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)

        def backtrack(i, curr):
            if i == n:
                output.append(curr[:])
                return

            # Include nums[i]
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            
            # Exclude nums[i]
            backtrack(i+ 1, curr)
        backtrack(0, [])

        return output