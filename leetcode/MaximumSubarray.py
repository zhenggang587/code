
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        s = A[0]
        max_sum = A[0]
        for i in range(1, len(A)):
            if s > 0:
                s += A[i]
            else:
                s = A[i]
            if s > max_sum:
                max_sum = s
        return max_sum
        
if __name__ == "__main__":
    s = Solution()

    print s.maxSubArray([-2])
