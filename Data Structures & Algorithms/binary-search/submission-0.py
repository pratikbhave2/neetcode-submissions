class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while end >= start and end >=0 and start <= len(nums) - 1:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                start += 1
            elif nums[mid] > target:
                end -= 1
        return -1