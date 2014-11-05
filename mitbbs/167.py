
class Solution:
    def getSolution(self, A):
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return min(A[0], A[1])

        n = len(A)
        m = n / 2
        if A[m] < A[m - 1] and A[m] < A[m + 1]:
            return A[m]
        elif A[m] > A[m - 1]:
            return self.getSolution(A[:m])
        else:
            return self.getSolution(A[m + 1:])

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 3, 7, 19, 8, 6, 11, 34, 23, 67])
