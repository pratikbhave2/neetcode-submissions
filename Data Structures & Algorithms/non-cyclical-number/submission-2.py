class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquares(num : int):
            ssq = 0
            while num !=0:
                digit = num %10
                ssq += (digit * digit)
                num //= 10
            return ssq


        seen = set()

        while True:
            n = sumofsquares(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)

