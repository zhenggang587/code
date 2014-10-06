
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0 for j in range(n)] for i in range(m)]
        if obstacleGrid[0][0]:
            return 0
        else:
            path[0][0] = 1
        for i in range(1, m):
            if not obstacleGrid[i][0]:
                path[i][0] = 1
            else:
                break
        for j in range(1, n):
            if not obstacleGrid[0][j]:
                path[0][j] = 1
            else:
                break


        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[m - 1][n - 1]
        
if __name__ == "__main__":
    s = Solution()

    print s.uniquePathsWithObstacles(
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
)
