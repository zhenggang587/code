
class Solution:
    # assume positive
    def getSolution(self, num):
        s = []
        while num > 0:
            s.append(num % 10)
            num /= 10
        s = s[::-1]

        n = len(s)
        if n % 2 == 1:
            l = r = n / 2
        else:
            r = n / 2
            l = r - 1
        i, j = l, r
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        if i < 0 or s[i] < s[j]:
            self.midAddOne(s, l, r)
        if len(s) == n: # not 9 -> 11
            self.setRightToLeft(s, l, r)    

        ret = 0
        for a in s:
            ret = ret * 10 + a
        return ret

    def setRightToLeft(self, num, i, j):
        n = len(num)
        while i >= 0:
            num[j] = num[i]
            i -= 1
            j += 1

    def midAddOne(self, num, l, r):
        tmp = min(num[l], num[r]) + 1
        num[l] = num[r] = tmp % 10
        if num[l] != 0:
            return
        
        n = len(num)
        l -= 1
        r += 1
        while l >= 0 and r < n:
            num[l] += 1
            num[r] += 1
            if num[l] != 0:
                break
            l -= 1
            r += 1
        if l < 0:
            del num[0]
            num.append(1)
            num.insert(0, 1)
                


if __name__ == "__main__":
    s = Solution()

    print s.getSolution(1)
    print s.getSolution(9)
    print s.getSolution(99)
    print s.getSolution(123)
    print s.getSolution(1234)
    print s.getSolution(4321)
    print s.getSolution(4992)
    print s.getSolution(4995)
    print s.getSolution(12345)
