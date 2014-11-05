
class Solution:
    def getSolution(self, A):
        left = [1 for a in A]
        for i in range(1, len(A)):
            left[i] = left[i - 1] * A[i - 1]

        ret = [1 for a in A]
        right = 1
        for i in range(len(A) - 1, -1, -1):
            ret[i] = left[i] * right
            right *= A[i]
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 3, 4, 5])
