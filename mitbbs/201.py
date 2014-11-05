
class Solution:
    def getSolution(self, num):
        ret = ''
        if num % 3 == 0:
            ret += 'fizz'
        if num % 5 == 0:
            ret += 'buzz'
        if not ret:
            return str(num)
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
