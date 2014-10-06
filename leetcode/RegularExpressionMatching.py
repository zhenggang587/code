
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        norm_p = self.mergeParttern(p)
        return self.matchPartial(s, 0, norm_p, 0) 

    def mergeParttern(self, p):
        norm_p = ''
        i = 0
        j = -1
        while i < len(p):
            if len(norm_p) > 0 and j - 1 >= 0 and p[i] == norm_p[j - 1] \
                and i + 1 < len(p) and p[i + 1] == '*' and j < len(norm_p) and norm_p[j] == '*':
                i += 2
            else:
                norm_p += p[i]
                j += 1
                i += 1
        return norm_p


    def matchPartial(self, s, index_s, p, index_p):
        if index_s == len(s):
            while index_p < len(p):
                if index_p + 1 < len(p) and p[index_p + 1] == '*':
                    index_p += 2
                else:
                    return False
            return True
        elif index_p >= len(p):
            return False

        if s[index_s] == p[index_p] or p[index_p] == '.':
            if index_p + 1 < len(p) and p[index_p + 1] != '*':
                return self.matchPartial(s, index_s + 1, p, index_p + 1)
            elif index_p + 1 < len(p) and p[index_p + 1] == '*':
                ret1 = self.matchPartial(s, index_s + 1, p, index_p + 2) # match 2
                if ret1:
                    return True
                ret2 = self.matchPartial(s, index_s + 1, p, index_p) # match -1
                if ret2:
                    return True
                ret3 = self.matchPartial(s, index_s, p, index_p + 2) # match zero
                return ret3
            else:
                return index_s + 1 == len(s)
        else:
            if index_p + 1 < len(p) and p[index_p + 1] == '*':
                return self.matchPartial(s, index_s, p, index_p + 2)
            else:
                return False


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
