
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        s = [[0 for col in range(len(matrix[row]))] for row in range(len(matrix))]
        s[0][0] = 1 if matrix[row][col] == '1' else 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == '1':
                    base = 0
                    if col > 0:
                        base = s[row][col - 1]
                    s[row][col] = base + 1
                


if __name__ == "__main__":
    s = Solution()

    print s.maximalRectangle()
