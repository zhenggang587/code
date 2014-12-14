
class Solution:
    def getSolution(self, A):
        if not A:
            return 0
            
        n = len(A)
        a = 0
        b = A[0]
        c = 0
        for i in range(2, n + 1):
            c = max(a + A[i - 1], b)
            a = b
            b = c

        return b

    def getSolution1(self, A):
        if not A:
            return 0

        n = len(A)
        f = [0 for i in range(n + 1)]
        f[1] = A[0]
        for i in range(1, n):
            f[i + 1] = max(f[i - 1] + A[i], f[i])

        return f[n]

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 5, 3, 4, 6])
