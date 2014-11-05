
class Solution:
    def getSolution(self, matrix, k):
        if not len(matrix) or not len(matrix[0]):
            return False
        m = len(matrix)
        n = len(matrix[0])

        i = m - 1
        j = 0
        while i >= 0 and j <= n:
            if matrix[i][j] == k:
                return True
            elif matrix[i][j] > k:
                i -= 1
            else:
                j += 1
        return False


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 3, 5], [2, 4, 7]], 5)
