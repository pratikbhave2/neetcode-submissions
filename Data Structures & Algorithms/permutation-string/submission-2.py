class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     # Hash table
    #     if len(s1) > len(s2):
    #         return False
    #     count_s1 = [0] * 26
    #     for c in s1:
    #         count_s1[ord(c) - ord('a')] += 1
    #     print("S1" , count_s1)
    #     need = len(s1)
    #     for i in range(0, len(s2) - need + 1):
    #         print("INSIDE", i)
    #         count_s2 = [0] * 26
    #         for j in range(need):
    #             count_s2[ord(s2[i + j]) - ord('a')] += 1
    #         # print("s2", count_s2)
    #         if count_s1 == count_s2:
    #             return True

    #     return False


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency count for characters in s1
        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        # Sliding window frequency count for s2
        count_s2 = [0] * 26
        window_size = len(s1)

        # Initialize the first window
        for i in range(window_size):
            count_s2[ord(s2[i]) - ord('a')] += 1

        # Check if the first window matches
        if count_s1 == count_s2:
            return True

        # Slide the window across s2
        for i in range(window_size, len(s2)):
            # Add the new character
            count_s2[ord(s2[i]) - ord('a')] += 1
            # Remove the old character
            count_s2[ord(s2[i - window_size]) - ord('a')] -= 1
            # Check if the current window matches
            if count_s1 == count_s2:
                return True

        return False