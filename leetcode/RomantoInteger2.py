
class Solution:
    # @return an integer
    def romanToInt(self, s):
        d = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        ret = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in d:
                ret += d[s[i:i+2]]
                i += 2
            else:
                ret += d[s[i:i+1]]
                i += 1
        return ret
                
        
if __name__ == "__main__":
    s = Solution()

    assert s.romanToInt('MMMCMXCIX') == 3999
    assert s.romanToInt('MDCCCXCIX') == 1899
    assert s.romanToInt('MD') == 1500
    assert s.romanToInt('CD') == 400
    assert s.romanToInt('XX') == 20
    assert s.romanToInt('V') == 5

