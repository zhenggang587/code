
class Solution:
    def getSolution(self, n):
        ret = []
        i = 2
        while i <= n:
            while n % i == 0:
                ret.append(i)
                n /= i
            i += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(12)
    print s.getSolution(13)
