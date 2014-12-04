
'''
given string S, judge whether it's equal to a substring T which repeats K times. T is unknown, K is unknown
for example: 
S = 'abcabc', return True, because T = 'abc', K = 2
S = 'ab', return False
'''

class Solution:
    def getSolution(self, s):
        next = self.getNext(s)
        n = len(s)
        i = n - 1
        while i >= 0 and next[i] != -1:
            i -= 1

        i += 1
        K = i
        j = 0
        while i < n and next[i] == j:
            i += 1
            j += 1
        if i == n and n % K == 0:
            return True
        return False

    def getNext(self, s):
        n = len(s)
        next = [-1 for i in range(n)]

        j = -1
        for i in range(1, n):
            while j != -1 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
                next[i] = j
        return next

if __name__ == "__main__":
    s = Solution()
    
    assert s.getSolution('aaaa') == True
    assert s.getSolution('abcabcabc') == True
    assert s.getSolution('abcabcab') == False
    assert s.getSolution('aaabaaab') == True
