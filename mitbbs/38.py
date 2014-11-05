
class Solution:
    def getSolution(self, A):
        s = sum(A) / 2

        n = len(A)
        f = [[set() for j in range(n + 1)] for i in range(n + 1)]
        f[0][0] = set([0])
        ret = -(1 << 31)
        for i in range(n):
            for j in range(i+1):
                f[i + 1][j + 1]  = f[i + 1][j + 1].union(f[i][j + 1])
                for num in f[i][j]:
                    f[i + 1][j + 1].add(num + A[i])
                for num in f[i + 1][j + 1]:
                    if num <= s:
                        ret = max(ret, num)
        return sum(A) - 2 * ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([5, 5, 2, 10, 2])
