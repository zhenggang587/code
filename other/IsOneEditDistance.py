'''
judge whether two string is one edit distance
abc adc return True
abc ac  return True
abc abdc return True
ab bc return False
'''

class Solution:
    def getSolution(self, s1, s2):
        return self.judge(s1, s2, False)

    def judge(self, s1, s2, flag):
        if not s1 and not s2:
            return flag
        elif not s1:
            return not flag and len(s2) == 1
        elif not s2:
            return not flag and len(s1) == 1

        if s1[0] == s2[0]:
            return self.judge(s1[1:], s2[1:], flag)
        else:
            if flag:
                return False
            return self.judge(s1[1:], s2, True) or self.judge(s1, s2[1:], True) or self.judge(s1[1:], s2[1:], True)


if __name__ == "__main__":
    s = Solution()

    assert s.getSolution('abc', 'adc') == True
    assert s.getSolution('abc', 'ac') == True
    assert s.getSolution('abc', 'abcc') == True
    assert s.getSolution('ab', 'bc') == False
    assert s.getSolution('a', '') == True 
    assert s.getSolution('a', 'a') == False
