class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        l = 0
        n = len(nums)
        for r in range(k, n + 1):
            # print(r)
            sub_list = nums[l: r]
            # print(sub_list)
            output.append(max(sub_list))
            l += 1
        # print(output) 
        return output  