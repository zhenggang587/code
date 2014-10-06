
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        s = sorted(S)

        paths = []
        path = []
        self.traverse(s, 0, path, paths)
        return paths

    def traverse(self, s, index, path, paths):
        paths.append(path[:])

        for i in range(index, len(s)):
            if i != index and s[i] == s[i - 1]:
                continue
            path.append(s[i])
            self.traverse(s, i + 1, path, paths)
            path.pop()
        
        
if __name__ == "__main__":
    s = Solution()

    print s.subsetsWithDup([1, 1, 2, 2])

