class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        result = nums[0]
        while r >= l:
            if nums[l] < nums[r]:
                result = min(result, nums[l])

            mid = (l + r) // 2

            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result


