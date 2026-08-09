class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bottom = ROWS
        left = 0
        right = COLS
        res = []
        

        while left < right and top < bottom:
            # Get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Get every i in the right most column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                return res
            
            # Get every i in the bottom most row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # Get every i in the left most column

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res



        
