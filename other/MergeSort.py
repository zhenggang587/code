
class Solution:
    def mergeSort(self, A):
        self._mergeSort(A, 0, len(A) - 1)

    def _mergeSort(self, A, left, right):
        if left >= right:
            return

        mid = left + (right - left) / 2
        self._mergeSort(A, left, mid)
        self._mergeSort(A, mid + 1, right)

        self.merge(A, left, mid, right)

    def merge(self, A, left, mid, right):
        l = A[left:mid+1]
        r = A[mid+1:right+1]

        for i in range(left, right + 1):
            if l and r:
                if l[0] < r[0]:
                    A[i] = l.pop(0)
                else:
                    A[i] = r.pop(0)
            elif l:
                A[i] = l.pop(0)
            elif r:
                A[i] = r.pop(0)

if __name__ == "__main__":
    s = Solution()

    A = [3, 1, 4]
    s.mergeSort(A)
    print A
