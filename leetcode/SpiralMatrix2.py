
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
        ret = []
        while True:
            for j in range(left, right + 1):
                ret.append(matrix[top][j])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                ret.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for j in range(right, left - 1, -1):
                ret.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                ret.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ret
            
        
if __name__ == "__main__":
    s = Solution()

    print s.spiralOrder([[1, 2]])
