
class Solution:
    def getSolution(self, A):
        n = len(A)
        self.shuffle(A, 0, n - 1) 
        return A

    def shuffle(self, A, l, r):
        if r - l <= 1:
            return

        m = l + (r - l) / 2
        lm = l + (m - l + 1) / 2
        rm = lm + (m - lm + 1) * 2 - 1
        self.reverse(A, lm, m, rm)

        if (m - l) % 2 == 1:
            self.shuffle(A, l, m)
            self.shuffle(A, m + 1, r)
        else:
            A[m], A[m + 1] = A[m + 1], A[m]
            self.shuffle(A, l, m - 1)
            self.shuffle(A, m + 2, r)

    def reverse(self, A, l, m, r):
        self._reverse(A, l, r)
        self._reverse(A, l, m)
        self._reverse(A, m + 1, r)
    
    def _reverse(self, A, l, r):
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1



if __name__ == "__main__":
    s = Solution()

    print s.getSolution([1, 3, 5, 2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    print s.getSolution([1, 3, 2, 4]) == [1, 2, 3, 4]
