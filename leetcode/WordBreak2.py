
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s:
            return True
            
        d = [False for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i+1] in dict and (j == 0 or d[j - 1]):
                    d[i] = True
                    break
        return d[len(s) - 1]


if __name__ == "__main__":
    s = Solution()

    assert s.wordBreak('a', ['a']) == True
    assert s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]) == True
    assert s.wordBreak('catsanddog', []) == False
    assert s.wordBreak('', ["cat", "cats", "and", "sand", "dog"]) == True
    assert s.wordBreak('catsa', ["cat", "cats", "and", "sand", "dog"]) == False
    assert s.wordBreak("baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    ) == False
