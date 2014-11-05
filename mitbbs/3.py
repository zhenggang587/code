
class Solution:
    def getSolution(self, A, B):
        p1 = 0
        p2 = 0
        ret = []
        while p1 < len(A) and p2 < len(B):
            if A[p1] == B[p2]:
                ret.append(A[p1])
                p1 += 1
                p2 += 1
            elif A[p1] < B[p2]:
                p1 += 1
            else:
                p2 += 1
        return ret[::-1]

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 3, 5], [2, 3, 5])
