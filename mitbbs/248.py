
class Solution:
    def getSolution(self, dict, target):
        t = str(target)
        i = 0
        while i < len(t):
            c = int(t[i])
            if i < len(t) - 1 and c in dict:
                i += 1
            else:
                return self.findLarge(dict, target, i)

    def findLarge(self, dict, target, i):
        t = str(target)
        c = int(t[i])
        n = self.findSmall(dict, c)
        while n == (1 << 31) and i > 0:
            i -= 1
            n = self.findSmall(dict, int(t[i]))
        if n == (1 << 31):
            n = min(dict)
            ret = 0
            while ret < target:
                ret = ret * 10 + n
            return ret
        else:
            ret = t[:i]
            ret += str(n)
            n = min(dict)
            for j in range(len(t) - i - 1):
                ret += str(n)
            return int(ret)

    def findSmall(self, dict, num):
        ret = (1 << 31)
        for a in dict:
            if a > num and a < ret:
                ret = a
        return ret
                    

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2], 11)
    print s.getSolution([1], 222)
    print s.getSolution([1, 5, 7], 56)
    print s.getSolution([1, 5], 56)
    print s.getSolution([1, 2], 0)
