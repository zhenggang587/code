
class Solution:
    def getSolution(self, s):
        n = len(s)
        if not n:
            return 0
        p = [[0 for j in range(n)] for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    p[i][j] = 0 if j - i < 2 else p[i + 1][j - 1] 
                else:
                    if i < n - 1:
                        p[i][j] = p[i + 1][j]
                    if j > 0:
                        p[i][j] = min(p[i][j], p[i][j - 1])
                    p[i][j] += 1

        return p[0][n - 1]

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('abbc')
