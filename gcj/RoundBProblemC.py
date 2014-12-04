
'''
d[i][j] = {d[i+1][k-1] and A[k] - A[i] == m and d[k+1][j-1] and A[j] - A[k] == m for i<k<j}


f[i] = min f[j - 1] if d[i][j] for j < i
'''

class Solution:
    def getSolution(self, A, m):
        n = len(A)
        d = [[False for j in range(n)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for k in range(i + 1, n):
                for j in range(k + 1, n):
                    if ((k - i < 3 or d[i + 1][k - 1]) and A[k] - A[i] == m) \
                        and ((j - k < 3 or d[k + 1][j - 1]) and A[j] - A[k] == m):
                        d[i][j] = True

        f = [i for i in range(n + 1)]
        for i in range(n):
            for j in range(i):
                if d[j][i]:
                    f[i + 1] = min(f[i + 1], f[j])
        return f[n]



if __name__ == "__main__":
    s = Solution()

    print s.getSolution([4, 4, 3, 3, 3, 4], 0)
    print s.getSolution([3, 1, 2, 3, 4], 1)
