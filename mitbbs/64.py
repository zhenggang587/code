
class Solution:
    def __init__(self):
        self.cnt = 0

    def getSolution(self, n):
        self.traverse(n, 0, 0, [])
        return self.cnt

    def traverse(self, n, i, j, path):
        if i == n - 1 and j == n - 1:
            self.cnt += 1
            return

        path.append((i, j))
        for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i1, j1 = i + x, j + y
            if i1 < 0 or i1 >= n or j1 < 0 or j1 >= n:
                continue
            if (i1, j1) in path:
                continue
            self.traverse(n, i1, j1, path)
        path.pop()

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(3)
