
class Solution:
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return

        m = len(matrix)
        n = len(matrix[0])
        queue = []
        for i in range(m):
            for j in [0, n - 1]:
                if matrix[i][j] == 1:
                    queue.append((i, j))

        for i in [0, m - 1]:
            for j in range(n):
                if matrix[i][j] == 1:
                    queue.append((i, j))

        while queue:
            row, col = queue.pop(0)
            matrix[row][col] = 2
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rowi, colj = row + i, col + j
                if rowi < 0 or rowi >= m  or colj < 0 or colj >= n:
                    continue
                if matrix[rowi][colj] == 1:
                    queue.append((rowi, colj))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 2:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1
        return matrix


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[0, 0, 0, 0],
                         [0, 1, 1, 0],
                         [0, 0, 1, 0],
                         [0, 1, 0, 0]])
