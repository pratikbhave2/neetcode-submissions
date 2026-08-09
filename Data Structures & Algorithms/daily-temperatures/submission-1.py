class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force
        # O ( n ^ 2) Time
        # O (n) Space

        # output = []
        # for i in range(0, len(temperatures)):
        #     found = False
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             output.append(j - i)
        #             found = True
        #             break
        #     if not found:
        #         output.append(0)

        # return output

        # Optimal
        n = len(temperatures)
        output = [0] * n
        stack = []

        for i in range(0, n):
            while (len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]):
                index = stack.pop()
                output[index] = i - index
            stack.append(i)

        return output

