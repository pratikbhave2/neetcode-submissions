class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force O(n square)
        # areas = []
        # for i in range(0, len(heights) - 1):
        #     for j in range(i + 1, len(heights)):
        #         max_height = min(heights[i], heights[j])
        #         max_width = j - i
        #         areas.append(max_height * max_width)
        # return max(areas)


        # Two pointers?
        areas = []
        start = 0
        end = len(heights) - 1
        while end > start:
            curr_area = (end - start) * min(heights[start], heights[end])
            areas.append(curr_area)

            if heights[start] <= heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
        
        return max(areas)