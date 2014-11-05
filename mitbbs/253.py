
class Solution:
    def getSolution(self, matrix, n, i, j):
        matrix = self.multiplyMatrix(matrix, n)
        return matrix[i][j]

    def multiplyMatrix(self, matrix, n):
        if n == 0:
            m = len(matrix)
            return [[1 if i == j else 0 for j in range(m)] for i in range(m)]
        if n == 1:
            return matrix

        sub = self.multiplyMatrix(matrix, n / 2)
        ret = self.multiply(sub, sub)
        if n % 2 == 1:
            ret = self.multiply(ret, matrix)
        return ret

    def multiply(self, A, B):
        m = len(A)
        ret = [[0 for j in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                for k in range(m):
                    ret[i][j] += A[i][k] * A[k][j]
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[0, 1, 1, 0],
                         [0, 0, 0, 1],
                         [0, 0, 0, 1],
                         [0, 0, 0, 0]], 2, 0, 3)
