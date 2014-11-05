
class Solution:
    def getSolution(self, A):
        m = {}
        ret = 0
        for i in range(len(A)):
            if A[i] not in m:
                m[A[i]] = i
            else:
                ret = max(ret, i - m[A[i]])
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 3, 2, 5, 4, 3])
