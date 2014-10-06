
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
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
                if board[i][j] < '1' or board[i][j] > '9':
                    return False

                if board[i][j] not in row[i]:
                    row[i].add(board[i][j])
                else:
                    return False

                if board[i][j] not in col[j]:
                    col[j].add(board[i][j])
                else:
                    return False

                sub_key = (i / 3) * 3 + j / 3
                if sub_key not in sub:
                    sub[sub_key] = set()
                if board[i][j] not in sub[sub_key]:
                    sub[sub_key].add(board[i][j])
                else:
                    return False
                
        return True
        
        
if __name__ == "__main__":
    s = Solution()

    print s.isValidSudoku([
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ])
