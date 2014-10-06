
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        dict_set = set(dict)
        path = [[] for i in range(len(s))]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in dict_set:
                    path[j].append(i)

        ret = []
        self.traverse(s, path, len(s) - 1, [], ret)

        return ret
                    
        
    def traverse(self, s, path, index, words, ret):
        if index < 0:
            ret.append(' '.join(words[::-1]))
            return

        for pre_index in path[index]:
            substr = s[pre_index:index+1]
            words.append(substr)
            self.traverse(s, path, pre_index - 1, words, ret)
            words.pop()



if __name__ == "__main__":
    s = Solution()

    print s.wordBreak('a', ['a'])
    print s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
    print s.wordBreak('catsanddog', [])
    print s.wordBreak('', ["cat", "cats", "and", "sand", "dog"])
    print s.wordBreak('catsa', ["cat", "cats", "and", "sand", "dog"])
