
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        paths = []
        path = []
        self.traverse(1, 0, n, k, path, paths)
        return paths

    def traverse(self, index, cur, n, k, path, paths):
        if cur == k:
            paths.append(path[:])
            return

        for i in range(index, n + 1):
            path.append(i)
            self.traverse(i + 1, cur + 1, n, k, path, paths)
            path.pop()
        
if __name__ == "__main__":
    s = Solution()

    print s.combine(4, 1)

