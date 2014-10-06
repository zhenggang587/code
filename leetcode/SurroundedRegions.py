
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        has_visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in has_visited:
                    self.bfs((i, j), board, has_visited)

    def bfs(self, index, board, has_visited):
        connected_list = []

        queue = []
        queue.append(index)
        has_visited.add(index)
        capture = True
        while queue:
            (x, y) = queue.pop(0)
            connected_list.append((x, y))
            if x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1:
                capture = False
            
            if x > 0 and board[x - 1][y] == 'O' and (x - 1, y) not in has_visited:
                queue.append((x - 1, y))
                has_visited.add((x - 1, y))
            if x < len(board) - 1 and board[x + 1][y] == 'O' and (x + 1, y) not in has_visited:
                queue.append((x + 1, y))
                has_visited.add((x + 1, y))
            if y > 0 and board[x][y - 1] == 'O' and (x, y - 1) not in has_visited:
                queue.append((x, y - 1))
                has_visited.add((x, y - 1))
            if y < len(board[0]) - 1 and board[x][y + 1] == 'O' and (x, y + 1) not in has_visited:
                queue.append((x, y + 1))
                has_visited.add((x, y + 1))

        for (x, y) in connected_list:
            if capture:
                board[x][y] = 'X'
        
if __name__ == "__main__":
    s = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X","O", "X", "X"]]


    s.solve(board)

    print board
