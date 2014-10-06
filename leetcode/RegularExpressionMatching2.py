
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        state = [[False for j in range(n + 1)] for i in range(m + 1)]
        state[0][0] = True
        for j in range(n):
            if p[j] == '*' and j > 0:
                state[0][j + 1] = state[0][j - 1]
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    state[i + 1][j + 1] = state[i][j]
                elif p[j] == '*':# match one and don't match
                    state[i + 1][j + 1] = state[i + 1][j] or state[i + 1][j - 1] \
                    or ((s[i] == p[j - 1] or p[j - 1] == '.') and state[i][j + 1]) # match many
            
        return state[m][n]


if __name__ == "__main__":
    s = Solution()

    assert s.isMatch('bbbba', '.*a*a') == True
    assert s.isMatch('a', 'ab*') == True
    assert s.isMatch('aaa', 'ab*a') == False
    assert s.isMatch('', '') == True
    assert s.isMatch('', 'a') == False
    assert s.isMatch('aa', '') == False
    assert s.isMatch('aa', 'a') == False
    assert s.isMatch('aa', 'aa') == True
    assert s.isMatch('aaa', 'aa') == False
    assert s.isMatch('aaa', 'aa*') == True
    assert s.isMatch('aaa', 'a.*') == True
    assert s.isMatch('ab', 'a.*') == True
    assert s.isMatch('aab', 'c*a*b') == True
