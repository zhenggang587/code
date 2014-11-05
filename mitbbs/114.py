
# f[n][m][s] = f[n - 1][m][s] union f[n][m - 1][s] and A[n]
class Solution:
    def getSolution(self, A, m, S):
        n = len(A)
        f = [[set([A[i - 1]]) if j == 1 and i != 0 else set() for j in range(n + 1)] for i in range(n + 1)]
        f[0][0] = set([0])

        for i in range(n):
            for j in range(i + 1):
                f[i + 1][j + 1] = f[i + 1][j + 1].union(f[i][j + 1])
                for a in f[i][j]:
                    f[i + 1][j + 1].add(a + A[i])

        dist = (1 << 31)
        ret = 0
        for a in f[n][m]:
            if a <= S and S - a < dist:
                dist = S - a
                ret = a
        return ret
            
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 3, 9, 15], 2, 13)
