
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False

        state = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                state[i + 1][0] = True
        for j in range(len(s2)):
            if s2[j] == s3[j]:
                state[0][j + 1] = True
        state[0][0] = True
        for i in range(len(s1)):
            for j in range(len(s2)):
                if (s1[i] == s3[i + j + 1] and state[i][j + 1]) or (s2[j] == s3[i + j + 1] and state[i + 1][j]):
                    state[i + 1][j + 1] = True

        return state[len(s1)][len(s2)]


if __name__ == "__main__":
    s = Solution()

    print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print s.isInterleave("aacaac", "aacaaeaac", "aacaaeaaeaacaac")
    print s.isInterleave("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    )
