class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force (O (n squared))

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                