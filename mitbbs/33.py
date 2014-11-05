
class Solution:
    def getSolution(self, A):
        if not A:
            return None

    def merge(self, A, l, r):
        if l >= r:
            return A[l:r+1]

        m = l + (r - l) / 2
        self.merge(A, l, m)
        self.merge(A, m + 1, r)

        i = l
        j = m + 1
        while i <= m and A[i] < 0:
            i += 1
        while j <= r and A[j] < 0:
            j += 1
        if m - i < r - j:
            k = m + 1
            while i <= m:
                A[i], A[k] = A[k], A[i]
                i += 1
                k += 1
        if k - i > 
        # in place 代码难写
            j = k
            


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
