
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board or not board[0]:
            return

        queue = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))  

        while queue:
            (x, y) = queue.pop(0)
            board[x][y] = 'C'
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xi, yj = x + i, y + j
                if xi < 0 or xi >= m or yj < 0 or yj >= n:
                    continue
                if board[xi][yj] == 'O':
                    queue.append((xi, yj))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'C':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
        

        
if __name__ == "__main__":
    s = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X","O", "X", "X"]]


    s.solve(board)

    print board
