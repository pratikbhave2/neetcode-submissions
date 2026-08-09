class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hash table
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1
        print("S1" , count_s1)
        need = len(s1)
        for i in range(0, len(s2) - need + 1):
            print("INSIDE", i)
            count_s2 = [0] * 26
            for j in range(need):
                count_s2[ord(s2[i + j]) - ord('a')] += 1
            print("s2", count_s2)
            if count_s1 == count_s2:
                return True

        return False
