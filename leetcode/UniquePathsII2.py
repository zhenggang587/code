
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0 for j in range(n + 1)] for i in range(m + 1)]
        path[0][1] = 1
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    path[i + 1][j + 1] = path[i][j + 1] + path[i + 1][j]
        return path[m][n]
        
if __name__ == "__main__":
    s = Solution()

    print s.uniquePathsWithObstacles(
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
)
