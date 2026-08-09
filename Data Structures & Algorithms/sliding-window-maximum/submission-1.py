class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # output = []

        # l = 0
        # n = len(nums)
        # for r in range(k, n + 1):
        #     # print(r)
        #     sub_list = nums[l: r]
        #     # print(sub_list)
        #     output.append(max(sub_list))
        #     l += 1
        # # print(output) 
        # return output 

        # using deque

        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

