
class Solution:
    def getSolution(self, n, w, h):
        p = [[0.0 for j in range(n + 1)] for i in range(n + 1)]
        p[n][0] = 1.0
        for i in range(n - 1, -1, -1):
            for j in range(n, -1, -1):
                if j > 0:
                    p[i][j] += p[i + 1][j - 1] * (i + 1) / (i + j)
                if j < n:
                    p[i][j] += p[i][j + 1] * (j + 1) / (i + j + 1)
        return p[w][h]

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(3, 1, 0)
