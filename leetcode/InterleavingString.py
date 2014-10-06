
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0 and len(s1) == 0 and len(s2) == 0:
            return True

        path = [[] for i in range(len(s3) + 1)]
        has_visited = set()
        path[0].append((-1, -1))
        has_visited.add((-1, -1))

        return self.traverse(s1, s2, s3, 0, path, has_visited)

    def traverse(self, s1, s2, s3, index, path, has_visited):
        if not path[index]:
            return False
        if index == len(s3):
            return True

        for (pre1, pre2) in path[index]:
            if pre1 + 1 < len(s1) and s1[pre1 + 1] == s3[index] and (pre1 + 1, pre2) not in has_visited:
                path[index + 1].append((pre1 + 1, pre2))
                has_visited.add((pre1 + 1, pre2))
                if self.traverse(s1, s2, s3, index + 1, path, has_visited):
                    return True
            if pre2 + 1 < len(s2) and s2[pre2 + 1] == s3[index] and (pre1, pre2 + 1) not in has_visited:
                path[index + 1].append((pre1, pre2 + 1))
                has_visited.add((pre1, pre2 + 1))
                if self.traverse(s1, s2, s3, index + 1, path, has_visited):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()

    print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print s.isInterleave("aacaac", "aacaaeaac", "aacaaeaaeaacaac")
    print s.isInterleave("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    )
