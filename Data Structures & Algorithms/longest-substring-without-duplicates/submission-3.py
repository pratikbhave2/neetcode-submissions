class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # Brute force
        # result = 0
        # for i in range(len(s)):
        #     str_set = set()
        #     for j in range(i, len(s)):
        #         if s[j] in str_set:
        #             break
        #         str_set.add(s[j])
        #     result = max(result, len(str_set))
        # return result
        
        # Sliding window

        str_set = set()
        left = 0
        result = 0
        for r in range(len(s)):
            while s[r] in str_set:
                str_set.remove(s[left])
                left += 1
            str_set.add(s[r])
            result = max(result, len(str_set))
        return result

        # Sliding window optimal (WTF?)