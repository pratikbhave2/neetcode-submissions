class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time = O(N)
        # Space = O(N)
        seen = [0] * len(nums)
        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1