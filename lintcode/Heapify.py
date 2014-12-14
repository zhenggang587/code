
class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        n = len(A)
        for i in range(n / 2, -1, -1):
            self.siftDown(A, i, n)

    def siftDown(self, A, i, n):
        j = 2 * i + 1
        while j < n:
            if j < n - 1 and A[j + 1] < A[j]:
                j += 1
            if A[i] <= A[j]:
                break
            A[i], A[j] = A[j], A[i]
            i = j
            j = 2 * i + 1


if __name__ == "__main__":
    s = Solution()

    A = [3, 2, 1, 4, 5]
    s.heapify(A)
    print A
