
class Solution:
    # @return a string
    def intToRoman(self, num):
        radix = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        ret = ''
        i = 0
        while num:
            cnt = num / radix[i]
            num %= radix[i]
            ret += symbol[i] * cnt
            i += 1

        return ret
        
if __name__ == "__main__":
    s = Solution()

    assert s.intToRoman(3999) == 'MMMCMXCIX'
    assert s.intToRoman(1899) == 'MDCCCXCIX'
    assert s.intToRoman(1500) == 'MD'
    assert s.intToRoman(400) == 'CD'
    assert s.intToRoman(20) == 'XX'
    assert s.intToRoman(5) == 'V'

