class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: simplest case
            if nums[mid] == target:
                return mid


            # Case 2 : left subarray is sorted:
            if nums[mid] >= nums[left]:
                # CHeck if target is between l and mid
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Case 3: right sub array is sorted
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1

                else:
                    right = mid - 1

        return -1