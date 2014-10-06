
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        slow = 0
        fast = 1
        while fast < len(A):
            if A[fast] != A[slow]:
                slow += 1
                A[slow] = A[fast]
            fast += 1
        A = A[:slow+1]
        return slow + 1
        
if __name__ == "__main__":
    s = Solution()

    A = [1, 1, 2]
    print s.removeDuplicates(A)
    print A
