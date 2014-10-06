
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s:
            return True
            
        dict = set(dict)
        words = [[False for j in range(len(s))] for i in range(len(s))]
        d = [False for i in range(len(s))]
        max_len = 1
        for word in dict:
            if len(word) > max_len:
                max_len = len(word)

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in dict:
                    words[i][j] = True       

        for i in range(len(s)):
            j = i - max_len if i - max_len > 0 else -1
            while j < i:
                if (j == -1 or d[j]) and words[j+1][i]:
                    d[i] = True
                    break
                j += 1
        return d[len(s) - 1]


if __name__ == "__main__":
    s = Solution()

    print s.wordBreak('a', ['a'])
    print s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
    print s.wordBreak('catsanddog', [])
    print s.wordBreak('', ["cat", "cats", "and", "sand", "dog"])
    print s.wordBreak('catsa', ["cat", "cats", "and", "sand", "dog"])
    print s.wordBreak("baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    )
