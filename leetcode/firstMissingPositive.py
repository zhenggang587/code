
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            num = A[i]
            while num > 0 and num <= len(A) and A[num - 1] != num:
                A[i] = A[num - 1]
                A[num - 1] = num
                num = A[i]
                 
        i = 0
        while i < len(A):
            if A[i] != i + 1:
                return i + 1
            i = i + 1

        return i + 1
     


if __name__ == "__main__":
    s = Solution()

    print s.firstMissingPositive([])
    print s.firstMissingPositive([1,2,0])
    print s.firstMissingPositive([3,4,-1,1])
    print s.firstMissingPositive([1,1])
    print s.firstMissingPositive([1])
