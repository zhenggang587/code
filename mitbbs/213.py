
# O(n^2)

class Solution:
    def getSolution(self, A):
        minVal = -(1 << 31)
        ret = 0
        for i in range(len(A) - 1):
            fIndex = sIndex = -1
            first = second = (1 << 31)
            for j in range(len(A)):
                if A[j] <= minVal:
                    continue
                if A[j] < first:
                    sIndex = fIndex
                    fIndex = j
                    second = first
                    first = A[j]
                elif A[j] < second:
                    sIndex = j
                    second = A[j]
            minVal = A[fIndex]
            if sIndex < fIndex:
                A = A[:sIndex] + A[sIndex + 1:] + [A[sIndex]]
                ret += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 1, 2, 4])
