
class Solution:
    def getSolution(self, n):
        ret = 0
        while n:
            n = n & (n - 1)
            ret += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(7)
