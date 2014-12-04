
class Solution:
    def __init__(self):
        self.maxCnt = 0
        self.maxStart = 0

    def getSolution(self, matrix):
        visitedMap = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i, j) not in visitedMap:
                    self.dfs(matrix, i, j, visitedMap)
        return self.maxStart, self.maxCnt + 1

    def dfs(self, matrix, row, col, visitedMap):
        if (row, col) in visitedMap:
            return visitedMap[(row, col)]

        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rowi, colj = row + i, col + j
            if rowi < 0 or rowi >= len(matrix) or colj < 0 or colj >= len(matrix):
                continue
            if matrix[rowi][colj] == matrix[row][col] + 1:
                cnt = self.dfs(matrix, rowi, colj, visitedMap) + 1
                visitedMap[(row, col)] = cnt
                if cnt > self.maxCnt or (cnt == self.maxCnt and matrix[row][col] < self.maxStart):
                    self.maxCnt = cnt
                    self.maxStart = matrix[row][col]
                return cnt

        visitedMap[(row, col)] = 0
        return 0
         
        


if __name__ == "__main__":
    s = Solution()
    print s.getSolution([[3, 4], [1, 2]])


    s = Solution()
    print s.getSolution([[1, 2, 9], [5, 3, 8], [4, 6, 7]])
