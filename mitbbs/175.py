
class Solution:
    def getSolution(self, n):
        ret = 0
        b = 1
        while n:
            a = n % 10
            if a > 7:
                a -= 1
            ret += a * b
            b *= 9
            n /= 10
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(18)
