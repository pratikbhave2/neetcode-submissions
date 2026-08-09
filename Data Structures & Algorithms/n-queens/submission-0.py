class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()          # Tracks occupied columns
        diagonals = set()     # Tracks occupied diagonals (row - col)
        anti_diagonals = set()  # Tracks occupied anti-diagonals (row + col)
        result = []           # Stores the final solutions
        board = [["."] * n for _ in range(n)]  # Initialize an empty board

        def isNotUnderAttack(row, col):
            if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                return False
            return True

        def placeQueen(row, col):
            # Place a queen on the board and mark the column, diagonal, and anti-diagonal
            board[row][col] = "Q"
            cols.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)

        def removeQueen(row, col):
            # Remove the queen and unmark the column, diagonal, and anti-diagonal
            board[row][col] = "."
            cols.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)

        def addSolution():
            # Append the current board configuration to the results
            result.append(["".join(row) for row in board])

        def backtrack(row=0):
            for col in range(n):
                if isNotUnderAttack(row, col):
                    placeQueen(row, col)
                    if row + 1 == n:
                        addSolution()
                    else:
                        backtrack(row + 1)
                    removeQueen(row, col)

        backtrack(0)
        return result