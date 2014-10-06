
class Solution:
    def buildheap(self, A):
        n = len(A)
        for i in range(n / 2 - 1, -1, -1):
            self.siftdown(A, i, n)

    def siftdown(self, A, i, n):
        j = 2 * i + 1
        while j < n:
            if j < n - 1 and A[j + 1] > A[j]:
                j += 1
            if A[i] >= A[j]:
                break
            A[i], A[j] = A[j], A[i]
            i = j
            j = 2 * i + 1

    def heapsort(self, A):
        self.buildheap(A)
        n = len(A)
        for i in range(n):
            A[0], A[n - i - 1] = A[n - i - 1], A[0]
            self.siftdown(A, 0, n - i - 1)


if __name__ == "__main__":
    s = Solution()

    A = [5, 2, 2, 4, 3]
    s.heapsort(A)
    print A
