
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A:
            return True

        can_jump = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if i + A[i] >= can_jump:
                can_jump = i     

        return can_jump == 0
        
if __name__ == "__main__":
    s = Solution()

    print s.canJump([2,3,1,1,4])
    print s.canJump([3,2,1,0,4])
    print s.canJump([2, 0, 0])
