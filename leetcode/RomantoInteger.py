
class Solution:
    # @return an integer
    def romanToInt(self, s):
        index = 0
        cnt = 0
        ret = 0
        while index < len(s) and s[index] == 'M':
            cnt += 1
            index += 1
        ret += cnt * 1000

        if index >= len(s):
            return ret
        if s[index] == 'C' and index + 1 < len(s) and s[index + 1] == 'M':
            ret += 900
            index += 2
        elif s[index] == 'C' and index + 1 < len(s) and s[index + 1] == 'D':
            ret += 400
            index += 2
        elif s[index] == 'D':
            ret += 500
            index += 1
        cnt = 0
        while index < len(s) and s[index] == 'C':
            cnt += 1
            index += 1
        ret += cnt * 100

        if index >= len(s):
            return ret
        if s[index] == 'X' and index + 1 < len(s) and s[index + 1] == 'C':
            ret += 90
            index += 2
        elif s[index] == 'X' and index + 1 < len(s) and s[index + 1] == 'L':
            ret += 40
            index += 2
        elif s[index] == 'L':
            ret += 50
            index += 1
        cnt = 0
        while index < len(s) and s[index] == 'X':
            cnt += 1
            index += 1
        ret += cnt * 10

        if index >= len(s):
            return ret
        if s[index] == 'I' and index + 1 < len(s) and s[index + 1] == 'X':
            ret += 9
            index += 2
        elif s[index] == 'I' and index + 1 < len(s) and s[index + 1] == 'V':
            ret += 4
            index += 2
        elif s[index] == 'V':
            ret += 5
            index += 1
        cnt = 0
        while index < len(s) and s[index] == 'I':
            cnt += 1
            index += 1
        ret += cnt
        return ret

        
if __name__ == "__main__":
    s = Solution()

    assert s.romanToInt('MMMCMXCIX') == 3999
    assert s.romanToInt('MDCCCXCIX') == 1899
    assert s.romanToInt('MD') == 1500
    assert s.romanToInt('CD') == 400
    assert s.romanToInt('XX') == 20
    assert s.romanToInt('V') == 5

