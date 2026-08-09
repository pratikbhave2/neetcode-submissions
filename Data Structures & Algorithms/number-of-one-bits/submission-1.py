class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        print(n)
        while n > 0:
            res += n & 1
            n = n >> 1 # divide by 2

        return res