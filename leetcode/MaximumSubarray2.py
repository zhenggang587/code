
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        return self.findMax(A, 0, len(A) - 1)

    def findMax(self, A, left, right):
        if left > right:
            return -(1 << 31)

        mid = left + (right - left) / 2

        cross_sum = self.findCrossMid(A, mid, left, right)
        left_sum = self.findMax(A, left, mid - 1)
        right_sum = self.findMax(A, mid + 1, right)
        max_sum = left_sum if left_sum > right_sum else right_sum

        return cross_sum if cross_sum > max_sum else max_sum


    def findCrossMid(self, A, mid, left, right):
        left_sum = 0
        left_max_sum = 0
        for i in range(mid - 1, left - 1, -1):
            left_sum += A[i]
            if left_sum > left_max_sum:
                left_max_sum = left_sum

        right_sum = 0
        right_max_sum = 0
        for i in range(mid + 1, right + 1):
            right_sum += A[i]
            if right_sum > right_max_sum:
                right_max_sum = right_sum

        ret = A[mid]
        if left_max_sum > 0:
            ret += left_max_sum
        if right_max_sum > 0:
            ret += right_max_sum
        return ret

        
if __name__ == "__main__":
    s = Solution()

    print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
