
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        size = 2 * (bottom + right)
        ret = []
        row = col = 0
        while size >= 0:
            if top > bottom or left > right:
                break
            if top == bottom:
                for i in range(left, right + 1):
                    ret.append(matrix[top][i])
                break
            if left == right:
                for i in range(top, bottom + 1):
                    ret.append(matrix[i][left])
                break
                
            index = 0
            while index < size:
                ret.append(matrix[row][col])
                if row == top:
                    if col + 1 > right:
                        row += 1
                        col = right
                    else:
                        col += 1
                elif col == right:
                    if row + 1 > bottom:
                        row = bottom
                        col = right - 1
                    else:
                        row += 1
                elif row == bottom:
                    if col - 1 < left:
                        row = bottom - 1
                        col = left
                    else:
                        col -= 1
                elif col == left:
                    if row - 1 <= top:
                        break
                    else:
                        row -= 1
                index += 1
            col += 1

            top += 1
            bottom -= 1
            left += 1
            right -= 1
            size -= 8

        return ret
            
        
if __name__ == "__main__":
    s = Solution()

    print s.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
