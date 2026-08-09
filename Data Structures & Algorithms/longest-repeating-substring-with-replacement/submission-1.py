class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Optimal
        # count = {}
        # result = 0
        # left = 0
        # most_freq_char_count = 0

        # for right in range(len(s)):
        #     count[s[right]] = 1 + count.get(s[right], 0)

        #     most_freq_char_count = max(most_freq_char_count, count[s[right]])

        #     while (right - left + 1) - most_freq_char_count > k:
        #         count[s[left]] -= 1
        #         left += 1

        #     result = max(result, right - left + 1)
        # return result


        # Brute force

        result = 0
        for i in range(len(s)):
            count = {}
            maxf = 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])

                if (j - i + 1) - maxf <= k:
                    result = max(result, j - i + 1)
        return result
        # res = 0
        # for i in range(len(s)):
        #     count, maxf = {}, 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         maxf = max(maxf, count[s[j]])
        #         if (j - i + 1) - maxf <= k:
        #             res = max(res, j - i + 1)
        # return res

