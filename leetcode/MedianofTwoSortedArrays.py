
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)
        if total % 2 == 1:
            return self.findKth(A, B, total / 2 + 1)
        else:
            return float(self.findKth(A, B, total / 2)
                        + self.findKth(A, B, total / 2 + 1)) / 2
                
    def findKth(self, A, B, k):
        if len(A) > len(B):
            return self.findKth(B, A, k)
        if len(A) == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pa = min(k / 2, len(A))
        pb = k - pa
        if A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa:], B, k - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.findKth(A, B[pb:], k - pb)
        else:
            return A[pa - 1]
        
if __name__ == "__main__":
    s = Solution()

    print s.findMedianSortedArrays([], [2, 4])
