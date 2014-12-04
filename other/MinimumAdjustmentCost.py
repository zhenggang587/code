
INT_MAX = (1 << 31)

class Solution:
    def getSolution(self, A, target):
        n = len(A)
        f = [[INT_MAX if i != 0 else 0 for j in range(101)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(101):
                l = max(0, j - target)
                r = min(100, j + target)
                for k in range(l, r + 1):
                    f[i][j] = min(f[i][j], f[i - 1][k])
                f[i][j] += abs(j - A[i - 1])
        
        return min(f[n])


if __name__ == "__main__":
    s = Solution()

    print s.getSolution([1, 4, 2, 3], 1)

