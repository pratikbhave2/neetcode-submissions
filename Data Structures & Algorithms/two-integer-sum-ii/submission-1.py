class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force (O (n squared))

        # for i in range(len(numbers) - 1):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        

        # Two pointers?
        start = 0
        end = len(numbers) - 1

        while (start < end) and end > 0 and start < len(numbers) and start != end:
            if (numbers[start] + numbers[end]) == target:
                return [start + 1, end + 1]
            if (numbers[start] + numbers[end] ) > target:
                end -= 1
            elif (numbers[start] + numbers[end] ) < target:
                start += 1
        
                