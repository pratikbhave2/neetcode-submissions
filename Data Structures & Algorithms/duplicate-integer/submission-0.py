class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # .count()? (O (n ^ 2))
        # Because we loop through nums once
        # and .count() loops again
        # for item in nums:
        #     if nums.count(item) > 1:
        #         return True
        # return False
         

        # O(n)
        # Define a dict:
        duplicate = {}
        for item in nums:
            if item not in duplicate:
                duplicate[item] = 1
            else:
                return True
        return False