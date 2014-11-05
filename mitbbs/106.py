
class Solution:
    def power(self, x, y):
        sign = False
        if y < 0:
            y = -y
            sign = True

        ret = self._power(x, y)
        if sign:
            return 1.0 / ret
        return ret

    def _power(self, x, y):
        if y == 0:
            return 1
        if y == 1:
            return x

        half = self._power(x, y / 2)
        if y % 2 == 0:
            return half * half
        else:
            return x * half * half

    def powerDouble(self, x, y):
        sign = False
        if y < 0:
            y = -y
            sign = True

        ret = self._power(x, int(y))
        d = y - int(y)
        l = 0.5
        tmp = self.sqrt(x)
        while d > 1e-6:
            if d >= l:
                ret *= tmp
                d -= l
            l /= 2
            tmp = self.sqrt(tmp)

        if sign:
            return 1.0 / ret
        return ret

    def sqrt(self, x):
        k = x / 2.0
        while abs(k * k - x) > 1e-6:
            k = k - (k * k - x) / (2 * k)
        return k
            

if __name__ == "__main__":
    s = Solution()
    
    print s.power(3, 3)
    print s.powerDouble(3, -3.5)
