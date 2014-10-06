
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        s = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for j in range(len(word2) + 1):
            s[0][j] = j
        for i in range(len(word1) + 1):
            s[i][0] = i
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    s[i + 1][j + 1] = s[i][j]
                else:
                    s[i + 1][j + 1] = s[i][j] if s[i][j] < s[i + 1][j] else s[i + 1][j]
                    s[i + 1][j + 1] = s[i + 1][j + 1] if s[i + 1][j + 1] < s[i][j + 1] else s[i][j + 1]
                    s[i + 1][j + 1] += 1
        return s[len(word1)][len(word2)]



if __name__ == "__main__":
    s = Solution()

    print s.minDistance('', '')
    print s.minDistance('abc', '')
    print s.minDistance('', 'abc')
    print s.minDistance('abc', 'abc')
    print s.minDistance('abc', 'ad')
    print s.minDistance('abc', 'acd')
    print s.minDistance('abc', 'abceeeee')
    print s.minDistance('abc', 'bceeeee')
