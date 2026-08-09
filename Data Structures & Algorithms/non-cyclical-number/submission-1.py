class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.get_sum_of_squares(n)
            if n == 1:
                return True
        return False


    def get_sum_of_squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            output += (digit ** 2)
            n = n // 10
        return output
        