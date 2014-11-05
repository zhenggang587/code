
class Solution:
    def getSolution(self, A):
        if not A:
            return
            
        n = len(A)
        a = 0
        b = A[0]
        c = 0
        for i in range(2, n + 1):
            c = max(a + A[i - 1], b)
            a = b
            b = c

        return b

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 5, 3, 4, 6])
