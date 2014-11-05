
class Solution:
    def getSolution(self, A):
        start = 0
        end = 0
        ret = 0
        while end < len(A):
            if A[end] != A[start]:
                ret = max(ret, end - start)
                start = end
            end += 1
        ret = max(ret, end - start)
        return ret
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 4, 4, 4, 2, 2, 3, 4])
