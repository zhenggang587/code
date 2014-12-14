
class Solution:
    def getSolution(self, num):
        if num == 0:
            return 'zero'
        ret = ''

        d = num / 1000
        if d > 0:
            ret += self.getHundred(d) + ' thousand '
            num %= 1000
            if num > 0 and num < 100:
                ret += 'and '
        ret += self.getHundred(num)
        if ret[-1] == ' ':
            return ret[:-1]
        return ret

    def getHundred(self, num):
        digit = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        ret = ''
        
        d = num / 100
        if d > 0:
            ret += digit[d] + ' hundred '
            num %= 100
            if num > 0 and num < 10:
                ret += 'and '
        d = num / 10
        if d > 1:
            ret += digit[d * 10] + ' '
            num %= 10
        
        if num >= 10 and num < 20:
            ret += digit[num] + ' '
        elif num > 0:
            ret += digit[num] + ' '
        return ret[:-1]
        


if __name__ == "__main__":
    s = Solution()

    assert s.getSolution(1000) == 'one thousand'
    assert s.getSolution(1001) == 'one thousand and one'
    assert s.getSolution(2000) == 'two thousand'
    assert s.getSolution(90000) == 'ninety thousand'
    assert s.getSolution(41000) == 'fourty one thousand'
