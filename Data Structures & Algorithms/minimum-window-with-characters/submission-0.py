class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute Force

        if t == "":
            return ""
        
        count_t = {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        res, resLen = [-1, -1], float('inf')

        for i in range(len(s)):
            count_s = {}
            for j in range(i, len(s)):
                count_s[s[j]] = 1 + count_s.get(s[j], 0)

                flag = True
                for c in count_t:
                    if count_t[c] > count_s.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""
