
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        s = sorted(S)

        paths = []
        path = []
        self.traverse(s, 0, path, paths)
        return paths

    def traverse(self, s, index, path, paths):
        if index == len(s):
            paths.append(path[::])
            return

        self.traverse(s, index + 1, path, paths)
        path.append(s[index])
        self.traverse(s, index + 1, path, paths)
        path.pop()
        
        
if __name__ == "__main__":
    s = Solution()

    print s.subsets([1, 2, 3])

