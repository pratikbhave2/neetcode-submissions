class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # If the first number is greater than 0 then all of them are greater than 0 so not possible to sum up to zero
                return res

            if i > 0 and a == nums[i - 1]:
                continue # To avoid duplicates


            l = i + 1 # initizlie the next number than current
            r = len(nums) - 1 # right pointer at the end

            while r > l:
                result = a + nums[l] + nums[r]
                if result > 0:
                    r -= 1

                elif result < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    # To avoid duplicates
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1

        return res