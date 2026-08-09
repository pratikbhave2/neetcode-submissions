class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        print(n)
        for i in range(32):
            bit = (n >> i) & 1 # GEt the bit from (n / 2^i) & 1. n // 2^ i ensures we go all the way till the Most significant bit
            res += (bit << (31 - i)) # Put it at 2^(31-i) value
        return res