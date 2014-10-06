
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        row = {}
        col = {}
        sub = {}
        for i in range(9):
            row[i] = set()
            for j in range(9):
                if j not in col:
                    col[j] = set()

                if board[i][j] == '.':
                    continue

                row[i].add(board[i][j])
                col[j].add(board[i][j])
                sub_key = (i / 3) * 3 + j / 3
                if sub_key not in sub:
                    sub[sub_key] = set()
                if board[i][j] not in sub[sub_key]:
                    sub[sub_key].add(board[i][j])

        self.traverse(board, 0, 0, row, col, sub)
        return board

    def traverse(self, board, row_index, col_index, row, col, sub):
        if col_index == 9:
            return self.traverse(board, row_index + 1, 0, row, col, sub)
        if row_index == 9:
            return True

        if board[row_index][col_index] != '.':
            return self.traverse(board, row_index, col_index + 1, row, col, sub)

        for i in range(1, 10):
            val = str(i)
            sub_key = (row_index / 3) * 3 + col_index / 3
            if sub_key not in sub:
                sub[sub_key] = set()
            if val in row[row_index] or val in col[col_index] or val in sub[sub_key]:
                continue

            board[row_index][col_index] = val
            row[row_index].add(val)
            col[col_index].add(val)
            sub[sub_key].add(val)

            if self.traverse(board, row_index, col_index + 1, row, col, sub):
                return True

            board[row_index][col_index] = '.'
            row[row_index].remove(val)
            col[col_index].remove(val)
            sub[sub_key].remove(val)
        return False
        

        
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
