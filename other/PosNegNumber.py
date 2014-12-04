
class Solution:
    def getSolution(self, A):
        l = 0
        r = len(A) - 1
        self.merge(A, l, r)
        return A

    def merge(self, A, l, r):
        if l > r:
            return -1
        if l == r:
            if A[l] < 0:
                return l
            else:
                return l + 1

        m = l + (r - l) / 2
        ls = self.merge(A, l, m)
        rs = self.merge(A, m + 1, r)

        if ls >= 0 and rs >= 0:
            self.reverse(A, ls, m)
            self.reverse(A, m + 1, rs - 1)
            self.reverse(A, ls, rs - 1)
            return ls + rs - (m + 1)
        else:
            return max(ls, rs)

    def reverse(self, A, l, r):
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([-1, 1, -2, -2, -4, -7])
