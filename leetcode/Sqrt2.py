
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0

        k = x / 2.0
        while abs(x - k * k) > 1e-6:
            k = k - (k * k - x) / (2 * k)
        return int(k)
        
if __name__ == "__main__":
    s = Solution()

    print s.sqrt(0)
    print s.sqrt(1)
    print s.sqrt(2)
    print s.sqrt(3)
    print s.sqrt(4)
    print s.sqrt(5)
    print s.sqrt(6)
    print s.sqrt(7)
    print s.sqrt(8)
    print s.sqrt(9)
