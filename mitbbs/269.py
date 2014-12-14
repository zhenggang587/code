
# assume n * n matrix

class Solution:
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
