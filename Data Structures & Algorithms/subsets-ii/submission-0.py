class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)
        nums.sort()

        def backtrack(i, curr):
            # Base case: If all elements are processed
            if i == len(nums):
                res.append(curr[:])
                return
            
            # Include the current element
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()  # Backtrack
            
            # Exclude the current element and skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res