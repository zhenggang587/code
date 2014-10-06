
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        top = 0
        bottom = len(matrix) - 1
        while top < bottom:
            size = bottom - top

            col_cnt = 0
            while col_cnt < size:
                cnt = 0
                row = top
                col = top + col_cnt
                cur = matrix[row][col]
                while cnt < 4:
                    last = cur
                    if cnt % 2 == 0:
                        temp_row = row
                        row = col
                        col = len(matrix) - 1 - temp_row
                    else:
                        temp_col = col
                        col = len(matrix) - 1 - row
                        row = temp_col
                    cur = matrix[row][col]
                    matrix[row][col] = last
                    cnt += 1
                col_cnt += 1


            top += 1
            bottom -= 1
        return matrix

       
if __name__ == "__main__":
    s = Solution()

    A = [
        [1]
    ]

    print s.rotate(A)

