
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        mid = left = 0
        right = x
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right
        
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
