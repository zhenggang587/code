
# follow up: 4个指针走

class Solution:
    def findKth(self, A, B, k):
        if len(A) > len(B):
            return self.findKth(B, A, k)
        if len(A) == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pa = min(len(A), k / 2)
        pb = k - pa
        if A[pa - 1] == B[pb - 1]:
            return A[pa - 1]
        elif A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa:], B, k - pa)
        else:
            return self.findKth(A, B[pb], k - pb)
            

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
