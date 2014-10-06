
# TLE

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if not self.isValid(board, i, j, str(k)):
                            continue
                        board[i][j] = str(k)
                        if self.solveSudoku(board):
                            return True
                        board[i][j] = '.'
                    return False

        return True

    def isValid(self, board, row, col, k):
        for i in range(9):
            if board[row][i] == k:
                return False
            if board[i][col] == k:
                return False

        left = col / 3 * 3
        top = row / 3 * 3
        for i in range(top, top + 3):
            for j in range(left, left + 3):
                if board[i][j] == k:
                    return False
        return True
        

        
if __name__ == "__main__":
    s = Solution()

    a = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]

    s.solveSudoku(a)
    print a
