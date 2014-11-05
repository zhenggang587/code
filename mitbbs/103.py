
class Solution:
    def getSolution(self, A, B):
        ret = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                ret.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 3, 5, 7], [2, 5, 7, 10])
