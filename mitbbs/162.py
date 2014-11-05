
class Solution:
    def getSolution(self, d):
        if not d:
            return None

        m = {}
        for i in range(len(d) - 1):
            j = 0
            while j < len(d[i]) and j < len(d[i + 1]):
                if d[i][j] != d[i + 1][j]:
                    c = d[i][j]
                    if c not in m:
                        m[c] = []
                    m[c].append(d[i + 1][j])
                    break
                j += 1

        indegree = {}
        for k, l in m.items():
            if k not in indegree:
                indegree[k] = 0
            for c in l:
                if c not in indegree:
                    indegree[c] = 0
                indegree[c] += 1

        ready = [k for k, cnt in indegree.items() if cnt == 0]
        ret = []
        while ready:
            c = ready.pop(0)
            ret.append(c)
            if c not in m:
                continue
            for l in m[c]:
                indegree[l] -= 1
                if indegree[l] == 0:
                    ready.append(l)
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['about', 'as', 'at','bus', 'buy'])
