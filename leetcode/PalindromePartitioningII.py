
# TLE, see c++

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        f = [0 for i in range(n+1)]
        p = [[0 for i in range(n)] for j in range(n)]
        for i in range(n+1):
            f[i] = n - i - 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or p[i+1][j-1] == 1):
                    p[i][j] = 1
                    f[i] = min(f[i], f[j+1] + 1)
        
        return f[0]
