class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # sub optimal
        # O(M * N ) time
        # O(M + N) space
        # ROWS = len(matrix)
        # COLS = len(matrix[0])

        # row_zero = [False] * ROWS
        # col_zero = [False] * COLS

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 0:
        #             row_zero[i] = True
        #             col_zero[j] = True
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if row_zero[r] or col_zero[c]:
        #             matrix[r][c] = 0


        # FOLLOWUP
        # O( M * N) time
        # O (1) space
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_zero = False # Or you can use col_zero = False to keep track columnwise
        # IDEA
        # When you encounter a 0 element
        # Set the (0th row, current col) element to 0
        # if r >0, then set the 0th column of every row to 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        # Loop over the matrix and check if the 0th row element or 0th col element is 0, if yes then set curr_row, curr_col to 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
            