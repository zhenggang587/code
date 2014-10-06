
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        paths = []
        path = []
        self.traverse(1, n, k, path, paths)
        return paths

    def traverse(self, index, n, k, path, paths):
        if len(path) == k:
            paths.append(path[::])
            return
        if index > n:
            return

        self.traverse(index + 1, n, k, path, paths)
        path.append(index)
        self.traverse(index + 1, n, k, path, paths)
        path.pop()
        
if __name__ == "__main__":
    s = Solution()

    print s.combine(4, 4)

