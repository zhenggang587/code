
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)

        left, right = 0, n - 1
        while left < right:
            for i in range(n):
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
        return matrix

       
if __name__ == "__main__":
    s = Solution()

    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print s.rotate(A)

