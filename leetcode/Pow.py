
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        signed = False
        if n < 0:
            n = -n
            signed = True

        ret = self._pow(x, n)
        if signed:
            return 1.0 / ret
        return ret


    def _pow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x

        half = self._pow(x, n / 2)
        if n % 2 == 1:
            return x * half * half
        return half * half
        
       
if __name__ == "__main__":
    s = Solution()

    print s.pow(0, 0) 
    print s.pow(2.0, 1) 
    print s.pow(2.0, 2) 
    print s.pow(-2.0, 3) 
    print s.pow(2.0, -2) 
