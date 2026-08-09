class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # sub optimal
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_zero = [False] * ROWS
        col_zero = [False] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if row_zero[r] or col_zero[c]:
                    matrix[r][c] = 0