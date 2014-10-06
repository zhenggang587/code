import string

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        queue = [start]
        hasVisited = set([start])
        l = len(start)
        p = {end:[]}
        d = {}
        for x in dict:
            d[x] = (1 << 31)
            p[x] = []
        d[start] = 0
        
        while queue:
            n = len(queue)
            for i in range(n):
                word = queue.pop(0)
                for j in range(l):
                    for c in string.lowercase:
                        tmp = word[:j] + c + word[j+1:]
                        if tmp == end:
                            p[end].append(word)
                            continue
                        if tmp in hasVisited and d[tmp] == d[word] + 1:
                            p[tmp].append(word)
                            continue
                        if tmp in dict and tmp not in hasVisited:
                            d[tmp] = d[word] + 1
                            queue.append(tmp)
                            hasVisited.add(tmp)
                            p[tmp].append(word)
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
    
    print s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"])
