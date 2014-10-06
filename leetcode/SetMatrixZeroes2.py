
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        first_row, first_col = 1, 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = 0
                break
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = 0
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        for i in range(len(matrix)):
            if first_col == 0:
                matrix[i][0] = 0
        for j in range(len(matrix[0])):
            if first_row == 0:
                matrix[0][j] = 0


        
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
