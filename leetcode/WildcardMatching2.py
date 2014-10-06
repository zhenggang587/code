

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        curs, curp = 0, 0
        match, star = 0, -1

        while curs < n:
            if curp < m and (s[curs] == p[curp] or p[curp] == '?'):
                curs += 1
                curp += 1
            elif curp < m and p[curp] == '*':
                star = curp
                curp += 1
                match = curs
            elif star != -1:
                match += 1
                curs = match
                curp = star + 1
            else:
                return False

        while curp < m and p[curp] == '*':
            curp += 1

        return curp == m

        
if __name__ == "__main__":
    s = Solution()

    assert s.isMatch('aa', 'a') == False
    assert s.isMatch('aa', 'aa') == True
    assert s.isMatch('aaa', 'aa') == False
    assert s.isMatch('aa', '*') == True
    assert s.isMatch('aa', 'a*') == True
    assert s.isMatch('ab', '?*') == True
    assert s.isMatch('aab', 'c*a*b') == False


