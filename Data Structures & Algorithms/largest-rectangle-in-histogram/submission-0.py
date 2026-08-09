class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            h = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= h:
                rightMost += 1
            
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= h:
                leftMost -= 1

            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, h * (rightMost - leftMost + 1))

        return maxArea