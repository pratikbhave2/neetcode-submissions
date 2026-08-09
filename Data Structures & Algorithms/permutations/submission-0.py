class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(curr):
            # Base case: If the current permutation has all elements
            if len(curr) == n:
                res.append(curr[:])  # Add a copy of the current permutation
                return
            
            for i in range(n):
                # Skip elements already in the current permutation
                if nums[i] in curr:
                    continue

                curr.append(nums[i])  # Include nums[i]
                backtrack(curr)  # Recurse
                curr.pop()  # Backtrack by removing nums[i]

        backtrack([])
        return res