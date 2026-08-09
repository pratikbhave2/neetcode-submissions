class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(M * N) time
        # O(M + N) space
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row = [False] * ROWS
        col = [False] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
                    
        
        for i in range(ROWS):
            for j in range(COLS):
                if row[i] == True or col[j] == True:
                    matrix[i][j] = 0
        