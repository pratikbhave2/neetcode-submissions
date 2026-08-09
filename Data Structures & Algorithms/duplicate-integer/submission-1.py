class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for item in nums:
            if item in unique:
                return True
            unique.add(item)
        return False