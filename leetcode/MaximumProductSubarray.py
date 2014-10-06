
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        ret, minp, maxp = A[0], A[0], A[0]
        for i in range(1, len(A)):
            a = minp * A[i]
            b = maxp * A[i]
            maxp = max(a, b, A[i])
            minp = min(a, b, A[i])
            ret = max(maxp, ret)
        return ret
 
if __name__ == "__main__":
    s = Solution()
    
    print s.maxProduct([2, 3, -2, 4])
