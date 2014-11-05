
class Solution:
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        hasVisited = set()
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and (i, j) not in hasVisited:
                    ret += 1
                    self.traverse(matrix, i, j, hasVisited)
        return ret

    def traverse(self, matrix, row, col, hasVisited):
        hasVisited.add((row, col))
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0) 
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rowi, colj = row + i, col + j
                if rowi < 0 or rowi >= len(matrix) or colj < 0 or colj >= len(matrix[0]):
                    continue
                if matrix[rowi][colj] != 1 or (rowi, colj) in hasVisited:
                    continue
                hasVisited.add((rowi, colj))
                queue.append((rowi, colj))


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 0, 1],
                         [1, 0, 1],
                         [0, 1, 1]])
