class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26

        for char in s:
            count1[ord('a') - ord(char)] += 1
        

        count2 = [0] * 26

        for char in t:
            count2[ord('a') - ord(char)] += 1


        return count1 == count2