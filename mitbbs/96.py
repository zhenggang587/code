import math

class Solution:
    def getSolution(self, n):
        hbit = 0
        while ((1 << hbit) < n):
            hbit += 1
        lbit = hbit - 1
        lval = (1 << lbit)
        hval = (1 << hbit)
        while abs(lval - n) > 1e-6:
            mbit = (lbit + hbit) / 2.0
            mval = math.sqrt(lval * hval)

            if mval < n:
                lbit = mbit
                lval = mval
            else:
                hbit = mbit
                hval = mval
        return lbit

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(13)
