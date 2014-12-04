
class Solution:
    def getSolution(self, matrix):
        n = len(matrix)
        f = matrix[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[j] = matrix[i][j] + max(f[j], f[j + 1])
        return f[0]


if __name__ == "__main__":
    s = Solution()

    print s.getSolution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
