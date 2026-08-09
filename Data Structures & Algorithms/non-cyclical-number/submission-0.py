class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        seen = set()

        while True:
            sum_of_squares = self.get_sum(n_str)
            if sum_of_squares == "1":
                return True
            if sum_of_squares in seen:
                return False
            seen.add(sum_of_squares)
            n_str = sum_of_squares


    def get_sum(self, n_str: str) -> str:
        sum_of_squares = 0
        for digit in n_str:
            sum_of_squares += int(digit) ** 2
        
        return str(sum_of_squares)