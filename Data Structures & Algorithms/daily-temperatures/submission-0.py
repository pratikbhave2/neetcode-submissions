class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # output = []

        # Brute Force
        output = []
        for i in range(0, len(temperatures)):
            found = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output.append(j - i)
                    found = True
                    break
            if not found:
                output.append(0)
        print(output)
        return output

