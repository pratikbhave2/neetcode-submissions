class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # output = []
        # n = len(nums)
        
        # def backtrack(start):
        #     if start == n:
        #         output.append(nums[:])  # Append a copy of the current permutation
        #         return
            
        #     for i in range(start, n):
        #         # Swap nums[start] with nums[i]
        #         nums[start], nums[i] = nums[i], nums[start]
                
        #         # Recurse for the next index
        #         backtrack(start + 1)
                
        #         # Backtrack: Undo the swap
        #         nums[start], nums[i] = nums[i], nums[start]
        
        # backtrack(0)
        # return output

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