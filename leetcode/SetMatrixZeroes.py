
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row_flag = col_flag = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_flag |= (1 << i)
                    col_flag |= (1 << j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if ((row_flag >> i) & 1) or ((col_flag >> j) & 1):
                    matrix[i][j] = 0

        
if __name__ == "__main__":
    s = Solution()

    matrix = [
    [0, 1, 2, 3],
    [1, 0, 3, 0],
    [2, 3, 4, 5],
    [5, 6, 7, 8]
    ]

    s.setZeroes(matrix)
    print matrix
