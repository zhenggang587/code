
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        num = 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        end = n * n
        row = 0
        col = 0
        top = 0
        bottom = n - 1
        while num <= end:
            matrix[row][col] = num
            if row == top:
                col += 1
                if col > bottom:
                    row += 1
                    col = bottom
            elif col == bottom:
                row += 1
                if row > bottom:
                    col -= 1
                    row = bottom
            elif row == bottom:
                col -= 1
                if col < top:
                    row -= 1
                    col = top
            elif col == top:
                row -= 1
            if row == top and col == top:
                top += 1
                bottom -= 1
                row = col = top

            num += 1

        return matrix
        
if __name__ == "__main__":
    s = Solution()

    print s.generateMatrix(1)
    print s.generateMatrix(2)
    print s.generateMatrix(3)
    print s.generateMatrix(4)
