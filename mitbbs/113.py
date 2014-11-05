
class Solution:
    def getSolution(self, A):
        n = len(A)
        m = n / 2
        f = [[set([A[i - 1]]) if j == 1 and i != 0 else set() for j in range(m + 1)] for i in range(n + 1)]
        f[0][0] = set([0])

        l = sum(A) / 2
        for i in range(n):
            maxj = min(i + 1, m)
            for j in range(maxj):
                f[i + 1][j + 1] = f[i + 1][j + 1].union(f[i][j + 1])
                for a in f[i][j]:
                    tmp = a + A[i]
                    if tmp <= l:
                        f[i + 1][j + 1].add(tmp)

        dist = (1 << 31)
        for a in f[n][m]:
            if a <= l and l - a < dist:
                dist = l - a
        return dist * 2


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 4, 9, 16])
