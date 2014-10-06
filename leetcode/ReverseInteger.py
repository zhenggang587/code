
class Solution:
    # @return an integer
    def reverse(self, x):
        signed = False
        if x < 0:
            signed = True
            x = -x

        ret = 0
        while x > 0:
            ret = ret * 10 + x % 10
            x /= 10

        if signed:
            return -ret
        return ret

        
if __name__ == "__main__":
    s = Solution()

    assert s.reverse(123) == 321
    assert s.reverse(0) == 0
    assert s.reverse(-123) == -321 
