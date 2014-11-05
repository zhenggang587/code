
class Solution:
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return None

        m = len(matrix)
        p = [len(matrix[i]) - 1 for i in range(m)]

        minVal = matrix[0][p[0]]
        while True:
            flag = True
            for i in range(m):
                if matrix[i][p[i]] != minVal:
                    flag = False
                while p[i] >= 0 and matrix[i][p[i]] > minVal:
                    p[i] -= 1
                if p[i] < 0:
                    return None
                minVal = min(minVal, matrix[i][p[i]])
            if flag:
                return minVal
        return None
            


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 2], [1, 3, 4], [-1, 0, 3]])
