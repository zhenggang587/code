
# see 113.py

'''
l = sum(A)
dp[i][j][k] = dp[i-1][j][k] or dp[i-1][j-1][k-A[i]] j <= i
dp[i][0][0] = True

traverse j from l / 2 to 0
if d[n][n / 2][j] == True:
    return sum(A) - 2 * j
'''
class Solution:
    def getSolution(self, A):
        l = sum(A) / 2
        n = len(A)
        m = n / 2
        dp = [[[True if j == 0 and k == 0 else False for k in range(l + 1)] for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            minj = min(i, m)
            for j in range(1, minj + 1):
                for k in range(l + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if k - A[i - 1] >= 0:
                        dp[i][j][k] |= dp[i - 1][j - 1][k - A[i - 1]]

        for j in range(l, -1, -1):
            if dp[n][m][j]:
                return sum(A) - 2 * j



if __name__ == "__main__":
    s = Solution()

    print s.getSolution([1, 4, 9, 16])
