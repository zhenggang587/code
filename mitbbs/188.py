
class Solution:
    def getSolution(self, num):
        sign = '+1'
        if num < 0:
            sign = '(-1)'
            num = -num

        p = 0
        while num % 2 == 0:
            p += 1
            num /= 2

        return sign + ' ' + str(num) + ' 2 ' + str(p)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(7)
