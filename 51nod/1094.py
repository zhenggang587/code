
class Solution:
    def getSolution(self, A, k):
        n = len(A)
        if not n:
            return None

        m = {0: -1}
        a = 0
        for i in range(n):
            a += A[i]
            m[a] = i
            if a - k in m:
                return m[a - k] + 1, i
        return None

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 3, 4, 5, 6], 1)
