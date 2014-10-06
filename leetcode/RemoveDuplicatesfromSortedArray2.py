
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        pos = 0
        for i in range(1, len(A)):
            if A[i] != A[pos]:
                pos += 1
                A[pos] = A[i]
        return pos + 1
        
if __name__ == "__main__":
    s = Solution()

    A = [1, 1, 2]
    print s.removeDuplicates(A)
    print A
