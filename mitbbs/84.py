
class Solution:
    def getSolution(self, A):
        ret = [0 for i in range(len(A))]
        val = 1
        while val <= len(A):
            i = 0
            while i < len(A):
                if A[i] == 0:
                    A[i] = -1
                    break
                A[i] -= 1
                i += 1
            ret[i] = val
            val += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 0, 1, 0])
