
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        l = [0 for i in range(n)]
        r = [n for i in range(n)]
        h = [0 for i in range(n)]
        ret = 0
        for i in range(m):
            left, right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                    l[j] = max(l[j], left)
                else:
                    left = j + 1
                    l[j] = 0
                    r[j] = n
                    h[j] = 0
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], right)
                    ret = max(ret, h[j] * (r[j] - l[j]))
                else:
                    right = j
        return ret

        
if __name__ == "__main__":
    s = Solution()

    print s.maximalRectangle(
    ['111', '001']
    )
