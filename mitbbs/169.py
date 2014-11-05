
class Solution:
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return None

        m = len(matrix)
        n = len(matrix[0])
        s = [[0 if i != 0 else matrix[i][j] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    s[i][j] = s[i - 1][j] + 1

        maxArea = 0
        for i in range(m):
            h = self.maxHeight(A[i])
            maxArea = max(maxArea, h)
        return maxArea


    def maxHeight(self, A):
        s = []
        ret = 0
        for i in range(len(A)):
            if not s or A[i] > A[s[-1]]:
                s.append(i)
            else:
                while s:
                    if A[s[-1]] < A[i]:
                        break
                    j = s.pop()
                    if s:
                        ret = max(ret, (i - s[-1] - 1) * A[j])
                    else:
                        ret = max(ret, i * A[j])
                s.append(i)

        while s:
            j = s.pop()
            if s:
                ret = max(ret, (len(A) - 1 - s[-1]) * A[j])
            else:
                ret = max(ret, len(A) * A[j])
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.maxHeight([2,1,5,6,2,3])
