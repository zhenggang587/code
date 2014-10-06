
class Solution:
    def quickSort(self, A):
        self.partition(A, 0, len(A) - 1)

    def partition(self, A, l, r):
        if l >= r:
            return

        i = l
        j = r
        x = A[l]
        while i < j:
            while A[j] >= x and j > i:
                j -= 1
            if i < j:
                A[i] = A[j]
                i += 1
            while A[i] <= x and i < j:
                i += 1
            if i < j:
                A[j] = A[i]
                j -= 1
        A[i] = x
                
        self.partition(A, l, i)
        self.partition(A, i + 1, r)



if __name__ == "__main__":
    s = Solution()

    A = [5, 1, 2, 4, 3]
    s.quickSort(A)
    print A
