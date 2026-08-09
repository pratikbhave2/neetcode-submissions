class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##Brute force ( O(n squared))
        # longest = 1
        # for num in nums:
        #     curr = num
        #     streak = 1
        #     while (curr + 1) in nums:
        #         curr = curr + 1
        #         streak += 1
        #     longest = max(streak, longest)
        # return longest


        longest = 0
        for num in nums:
            # check if it is start of the sequence
            if (num - 1) not in nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest