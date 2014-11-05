
# best solution: O(n^3) dp[i][j][x][y], i + j = x + y = k => so dp[i][x][k] j = k - i, y = k - x

class Solution:
    def getSolution(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        d = [[[[0 for y in range(n)] for x in range(m)] for j in range(n)] for i in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                for x in range(m - 1, -1, -1):
                    for y in range(n):
                        if i < m - 1 and x < m - 1: 
                            d[i][j][x][y] = max(d[i][j][x][y], d[i + 1][j][x + 1][y])
                        if i < m - 1 and y > 0: 
                            d[i][j][x][y] = max(d[i][j][x][y], d[i + 1][j][x][y - 1])
                        if j > 0 and y > 0: 
                            d[i][j][x][y] = max(d[i][j][x][y], d[i][j - 1][x][y - 1])
                        if j > 0 and x < m - 1: 
                            d[i][j][x][y] = max(d[i][j][x][y], d[i][j - 1][x + 1][y])
                        if i == x and j == y:
                            d[i][j][x][y] += matrix[i][j]
                        else:
                            d[i][j][x][y] += matrix[i][j] + matrix[x][y]
        return d[0][n - 1][0][n - 1]


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 2, 3],
                         [5, 3, 4],
                         [8, 7, 0]])
