
class Solution:
    # @return a string
    def intToRoman(self, num):
        ret = ''

        cnt = num / 1000
        while cnt > 0:
            ret = ret + 'M'
            cnt -= 1
        num %= 1000

        cnt = num / 100
        if cnt == 9:
            ret = ret + 'CM'
        elif cnt >= 5:
            ret = ret + 'D'
            cnt -= 5
            while cnt > 0:
                ret = ret + 'C'
                cnt -= 1
        elif cnt == 4:
            ret = ret + 'CD'
        elif cnt > 0:
            while cnt > 0:
                ret = ret + 'C'
                cnt -= 1
        num %= 100

        cnt = num / 10
        if cnt == 9:
            ret = ret + 'XC'
        elif cnt >= 5:
            ret = ret + 'L'
            cnt -= 5
            while cnt > 0:
                ret = ret + 'X'
                cnt -= 1
        elif cnt == 4:
            ret = ret + 'XL'
        elif cnt > 0:
            while cnt > 0:
                ret = ret + 'X'
                cnt -= 1
        num %= 10

        cnt = num
        if cnt == 9:
            ret = ret + 'IX'
        elif cnt >= 5:
            ret = ret + 'V'
            cnt -= 5
            while cnt > 0:
                ret = ret + 'I'
                cnt -= 1
        elif cnt == 4:
            ret = ret + 'IV'
        elif cnt > 0:
            while cnt > 0:
                ret = ret + 'I'
                cnt -= 1
        return ret
        
if __name__ == "__main__":
    s = Solution()

    assert s.intToRoman(3999) == 'MMMCMXCIX'
    assert s.intToRoman(1899) == 'MDCCCXCIX'
    assert s.intToRoman(1500) == 'MD'
    assert s.intToRoman(400) == 'CD'
    assert s.intToRoman(20) == 'XX'
    assert s.intToRoman(5) == 'V'

