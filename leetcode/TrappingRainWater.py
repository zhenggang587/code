
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A) <= 2:
            return 0

        left_height = [a for a in A]
        left_max_height = A[0]
        for i in range(1, len(A) - 1):
            if left_max_height < A[i]:
                left_max_height = A[i]
            else:
                left_height[i] = left_max_height

        right_height = [a for a in A]
        right_max_height = A[len(A) - 1]
        for i in range(len(A) - 2, 0, -1):
            if right_max_height < A[i]:
                right_max_height = A[i]
            else:
                right_height[i] = right_max_height

        ret = 0
        for i in range(1, len(A) - 1):
            ret += min(left_height[i], right_height[i]) - A[i]
        return ret
        
if __name__ == "__main__":
    s = Solution()

    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
