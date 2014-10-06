
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0

        path = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[m - 1][n - 1]
        
if __name__ == "__main__":
    s = Solution()

    print s.uniquePaths(2, 3)
