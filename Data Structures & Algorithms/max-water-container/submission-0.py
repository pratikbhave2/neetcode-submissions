class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force O(n square)
        areas = []
        for i in range(0, len(heights) - 1):
            for j in range(i + 1, len(heights)):
                max_height = min(heights[i], heights[j])
                max_width = j - i
                areas.append(max_height * max_width)
        print(areas)
        return max(areas)
                