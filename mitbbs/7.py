
class Solution:
    def getSolution(self, s, dict):
        n = len(s)
        d = {}
        for i in range(n):
            d[i] = []
            for j in range(i, n):
                if s[i:j+1] in dict:
                    d[i].append(j)

        path = []
        paths = []
        self.traverse(s, 0, d, path, paths)
        return paths

    def traverse(self, s, index, d, path, paths):
        if index == len(s):
            paths.append(" ".join(path))
            return

        for next in d[index]:
            path.append(s[index:next + 1])
            self.traverse(s, next + 1, d, path, paths)
            path.pop()



if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution("thisisdesktop", ["this", "is", "desk", "top", "desktop"])
