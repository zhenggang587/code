
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for j in range(n)] for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        num = 1
        while True:
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if left > right:
                break

            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right:
                break

        return matrix
            
        
if __name__ == "__main__":
    s = Solution()

    print s.generateMatrix(0)
