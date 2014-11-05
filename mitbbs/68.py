
class Solution:
    def getSolution(self, start, end, dict):
        
        d = {}
        p = {end:[]}
        for w in dict:
            d[w] = (1 << 31)
            p[w] = []
        d[start] = 0

        queue = [start]
        hasVisited = set([start]
        while queue:
            n = len(queue)
            for i in range(n):
                word = queue.pop(0)
                for j in range(len(word)):
                    for c in string.lowercase:
                        tmp = word[:j] + c word[j+1:]
                        if tmp == end:
                            p[end].append(word)
                            continue
                        if tmp in hasVisited and d[tmp] == d[word] + 1:
                            p[tmp].append(word)
                            continue
                        if tmp in dict and tmp not in hasVisited:
                            queue.append(tmp)
                            hasVisited.add(tmp)
                            d[tmp] = d[word] + 1
            if p[end]:
                break

        paths = []
        self.traverse(start, end, p, [end], paths)
        return paths

    def traverse(self, start, cur, p, path, paths):
        if cur == start:
            paths.append(path[::-1])
            return

        for pre in p[cur]:
            path.append(pre)
            self.traverse(start, pre, p, path, paths)
            path.pop()

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
