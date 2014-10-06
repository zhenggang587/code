
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
        if index == len(s):
            paths.append(path[::])
            return

        end_index = index + 1
        while end_index < len(s) and s[end_index] == s[index]:
            end_index += 1
        self.traverse(s, end_index, path, paths)
        for i in range(index, end_index):
            path.append(s[i])
            self.traverse(s, end_index, path, paths)
        for i in range(index, end_index):
            path.pop()
        
        
if __name__ == "__main__":
    s = Solution()

    print s.subsetsWithDup([1, 1, 2, 2])

