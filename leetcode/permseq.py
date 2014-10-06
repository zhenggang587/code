

class Solution:
    def permnum(self, n):
        num = 1
        for i in range(1, n + 1):
            num = num * i
        return num

    # @return a string
    def getPermutation(self, n, k):
        ret = ''
        k = k - 1
        t = n - 1
        d = self.permnum(t)

        v = [i for i in range(1, n + 1)]

        while t > 0 and k != 0:
           i = k / d 
           ret = ret + str(v[i])
           del v[i]
           k = k % d
           d = d / t
           t = t - 1
        if k == 0:
            for c in v:
                ret = ret + str(c)

        return ret
        

if __name__ == "__main__":
    s = Solution()
    print s.getPermutation(3, 1)
    print s.getPermutation(3, 2)
    print s.getPermutation(3, 3)
    print s.getPermutation(3, 4)
    print s.getPermutation(3, 5)
    print s.getPermutation(3, 6)
