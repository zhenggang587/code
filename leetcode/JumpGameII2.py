
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A): 
        if len(A) <= 1:
            return 0

        tmp = right = A[0]
        cnt = 1 
        for i in range(1, len(A)):
            if i > right:
                right = tmp 
                cnt += 1
            if i + A[i] > tmp:
                tmp = i + A[i]

        if right >= len(A) - 1:
            return cnt 
        return -1 
        
if __name__ == "__main__":
    s = Solution()

    assert s.jump([2,3,1,1,4]) == 2
    assert s.jump([1, 1, 1, 1]) == 3
    assert s.jump([1]) == 0
