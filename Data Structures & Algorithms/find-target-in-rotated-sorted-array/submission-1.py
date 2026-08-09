class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # left = 0
        # right = n - 1

        # while left <= right:
        #     mid = left + (right - left) // 2

        #     # Case 1: simplest case
        #     if nums[mid] == target:
        #         return mid


        #     # Case 2 : left subarray is sorted:
        #     if nums[mid] >= nums[left]:
        #         # CHeck if target is between l and mid
        #         if target >= nums[left] and target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     # Case 3: right sub array is sorted
        #     else:
        #         if target <= nums[right] and target > nums[mid]:
        #             left = mid + 1

        #         else:
        #             right = mid - 1

        # return -1

        ## REcursion?

        return self.helper(nums, target, left=0, right=len(nums) - 1)


    def helper(self, nums: List[int], target: int, left=int, right=int) -> int:
        if left > right:
            return -1

        mid = left + (right - left) // 2
        # Simplest case
        if nums[mid] == target:
            return mid
        

        # Check if left array is sorted
        if nums[left] <= nums[mid]:
            # Check if target is between left and mid
            if (target >= nums[left] and target <= nums[mid]):
                return self.helper(nums, target, left, mid - 1)
            else:
                return self.helper(nums, target, mid + 1, right)
                 
        else:
            if target <= nums[right] and target > nums[mid]:
                return self.helper(nums, target, mid + 1, right)
            else:
                return self.helper(nums, target, left, mid - 1)

            