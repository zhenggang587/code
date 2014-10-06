
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not len(grid) or not len(grid[0]):
            return 0

        m = len(grid)
        n = len(grid[0])
        path = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            path[i][0] = path[i - 1][0] + grid[i][0]
        for j in range(1, n):
            path[0][j] = path[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = min(path[i - 1][j], path[i][j - 1]) + grid[i][j]

        return path[m - 1][n - 1]
        
if __name__ == "__main__":
    s = Solution()

    print s.minPathSum(
[
  [1,2],
  [1,1],
]
)
