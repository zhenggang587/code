
class Solution:
    def getSolution(self, A, B, C):
        p1, p2, p3 = 0, 0, 0
        ret = []
        while p1 < len(A) and p2 < len(B) and p3 < len(C):
            minV = min(A[p1], B[p2], C[p3])
            maxV = max(A[p1], B[p2], C[p3])
            if minV == maxV:
                ret.append(A[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if A[p1] < maxV:
                    p1 += 1
                if B[p2] < maxV:
                    p2 += 1
                if C[p3] < maxV:
                    p3 += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 5, 10], [2, 5, 6], [5, 6])
