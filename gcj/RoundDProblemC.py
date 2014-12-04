
class Solution:
    def getSolution(self, tickets):
        indegree = {}
        out = {}
        for (src, dst) in tickets:
            if src not in out:
                out[src] = []
            out[src].append(dst)
            if dst not in out:
                out[dst] = []

            if src not in indegree:
                indegree[src] = 0
            if dst not in indegree:
                indegree[dst] = 0
            indegree[dst] += 1

        ready = [node for node, d in indegree.items() if d == 0]
        ret = []
        while ready:
            node = ready.pop(0)
            for o in out[node]:
                indegree[o] -= 1
                if indegree[o] == 0:
                    ret.append(node + '-' + o)
                    ready.append(o)
        return ' '.join(ret)
        


if __name__ == "__main__":
    s = Solution()
    print s.getSolution([('SFO', 'DFW')])


    s = Solution()
    print s.getSolution([('MIA', 'ORD'), ('DFW', 'JFK'), ('SFO', 'DFW'), ('JFK', 'MIA')])
