
INT_MAX = (1 << 31)

class Solution:
    def getSolution(self, matrix, x, y):
        n = len(matrix)
        # f means the first i person run j's task a and k's task b, the min time
        f = [[[INT_MAX for k in range(y + 1)] for j in range(x + 1)] for i in range(n + 1)]
        f[0][0][0] = 0
        for i in range(n):
            for j in range(x + 1):
                for k in range(y + 1):
                    for a in range(j + 1):
                        for b in range(k + 1):
                            f[i + 1][j][k] = min(f[i + 1][j][k], max(f[i][j - a][k - b], a * matrix[i][0] + b * matrix[i][1]))
        return f[n][x][y]

    def getSolution1(self, matrix, x, y):
        n = len(matrix)
        low = 0
        high = matrix[0][0] * x + matrix[0][1] * y
        while low < high:
            mid = low + (high - low) / 2
            if self.can(matrix, x, y, mid):
                high = mid
            else:
                low = mid + 1
        return low

    def can(self, matrix, x, y, t):
        n = len(matrix)
        # f means the first i person run j's task b, the max number they can run task b with given time t
        f = [[-INT_MAX for j in range(x + 1)] for i in range(n + 1)]
        f[0][0] = 0
        for i in range(n):
            for j in range(x + 1):
                for k in range(j + 1):
                    f[i + 1][j] = max(f[i + 1][j], f[i][k] + (t - (j - k) * matrix[i][0]) / matrix[i][1])
        return f[n][x] >= y


if __name__ == "__main__":
    s = Solution()

    print s.getSolution([[1, 10], [10, 1]], 2, 2)
    print s.getSolution([[1, 1], [10, 10]], 2, 2)
    print s.getSolution([[2, 7], [5, 5], [7, 2]], 3, 3)

    print s.getSolution1([[1, 10], [10, 1]], 2, 2)
    print s.getSolution1([[1, 1], [10, 10]], 2, 2)
    print s.getSolution1([[2, 7], [5, 5], [7, 2]], 3, 3)
