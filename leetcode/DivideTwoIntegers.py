
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if not divisor:
            return None

        signed = 1
        if dividend < 0:
            dividend = -dividend # may overflow
            signed = -signed
        if divisor < 0:
            divisor = -divisor
            signed = -signed

        ret = 0
        count = 0
        sum = 0
        while divisor <= dividend:
            count = 1
            sum = divisor
            while sum + sum <= dividend:
                sum += sum
                count += count
            dividend -= sum
            ret += count

        if signed == -1:
            return -ret
        return ret
        
if __name__ == "__main__":
    s = Solution()

    print s.divide(-1, 1)
