
INT_MAX = (1 << 31)

class Solution:
    def getSolution(self, A):
        n = len(A)
        sum = [0 for i in range(n + 1)]
        sum[0] = A[0]
        for i in range(1, n):
            sum[i] = sum[i - 1] + A[i]

        f = [[0 if i == j else INT_MAX for j in range(n)] for i in range(n)]
        for v in range(1, n):
            for i in range(n - v):
                j = i + v
                for k in range(i, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])
                f[i][j] += sum[j] - (sum[i - 1] if i > 0 else 0)
        return f[0][n - 1]

if __name__ == "__main__":
    s = Solution()

    print s.getSolution([100])
    print s.getSolution([3, 4, 3])
    print s.getSolution([1, 1, 1, 1])
