
class Solution:
    def getTop(self, A, k):
        self.partition(A, 0, len(A) - 1, k)
        return A[:k]

    def partition(self, A, l, r, k):
        if l > r:
            return

        i = l
        j = r
        x = A[l]
        while i < j:
            while A[j] >= x and j > i:
                j -= 1
            A[i] = A[j]
            while A[i] <= x and i < j:
                i += 1
            A[j] = A[i]
        A[i] = x
        
        m = i - l + 1
        if m == k:
            return
        elif m > k:
            self.partition(A, l, i - 1, k)
        else:
            self.partition(A, i + 1, r, k - m)


if __name__ == "__main__":
    s = Solution()

    A = [5, 1, 2, 4, 3]
    print s.getTop(A, 3)
