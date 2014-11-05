
class Solution:
    def getSolution(self, board):
        if not board or not board[0]:
            return []

        m = len(board)
        n = len(board[0])
        paths = []
        for i in range(m):
            for j in range(n):
                hasVisited = set()
                path = [(i, j)]
                self.traverse(board, i, j, path, paths)
        return paths


    def traverse(self, board, row, col, path, paths):
        paths.append(path[:])

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                rowi, colj = row + i, col + j
                if rowi < 0 or rowi >= len(board) or colj < 0 or colj >= len(board[0]):
                    continue
                if (rowi, colj) in path:
                    continue
                path.append((rowi, colj))
                self.traverse(board, rowi, colj, path, paths)
                path.pop()
        
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 2], [4, 5]])
