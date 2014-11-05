#encoding:utf8

## d[i][j]的含义是到第i个时用了j个word的次数

class Solution:
    def getSolution(self, m, n):
        d = [[0 for j in range(m + 1)] for i in range(n + 1)]
        d[0][0] = 1
        for i in range(1, n + 1):
            k = min(i, m)
            for j in range(1, k + 1):
                d[i][j] = (d[i - 1][j] * j) % 1000000007 + d[i - 1][j - 1] * (m - j + 1) % 1000000007
                d[i][j] %= 1000000007
        return d[n][m]


if __name__ == "__main__":
    s = Solution()

    print s.getSolution(15, 15)
