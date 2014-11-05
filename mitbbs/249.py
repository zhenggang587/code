
class Solution:
    def getSolution(self, s, dict):
        n = len(s)
        d = [[] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] in dict:
                    d[i].append(j)

        paths = []
        self.traverse(d, 0, s, [], paths)
        return paths

    def traverse(self, d, index, s, path, paths):
        if index == len(s):
            paths.append(path[:])
            return

        for next in d[index]:
            path.append(s[index:next+1])
            self.traverse(d, next + 1, s, path, paths)
            path.pop()

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('fireman', ['a', 'an', 'em', 'fir', 'fire', 'ire', 'ma', 'man'])
