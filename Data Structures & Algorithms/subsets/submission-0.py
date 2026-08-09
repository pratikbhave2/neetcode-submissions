class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time = O (N * 2 ^N)
        output = []
        n = len(nums)

        def backtrack(i, curr):
            if i == n:
                output.append(curr[:])
                return
            
            backtrack(i + 1, curr)
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    
        backtrack(0, [])
        return output
        