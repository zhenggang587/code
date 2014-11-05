
class Solution:
    def getSolution(self, A, day):
        n = len(A)
        f = [[0 for j in range(n + 2)] for i in range(day + 1)]
        ret = 0
        for i in range(1, day + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i - 1][j - 1], f[i - 1][j + 1]) + A[j - 1]
                if i == day:
                    ret = max(ret, f[i][j])

        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 1, 4, 2], 3)
