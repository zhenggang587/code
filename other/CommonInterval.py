
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class MultiTreeNode:
    def __init__(self, x):
        self.val = x
        self.children = [None for i in range(4)]
        self.left = None
        self.right = None

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'


class Solution:
    def getSolution(self, vector):
        if not vector:
            return []

        base = sorted(vector[0], key=lambda x:x.start)
        i = 1
        while i < len(base):
            if base[i].start > base[i - 1].end:
                i += 1
            else:
                if base[i].end > base[i - 1].end:
                    base[i - 1].end = base[i].end
                base.pop(i)

        for i in range(1, len(vector)):
            tmp = []
            for interval in vector[i]:
                j = 0
                while j < len(base):
                    if interval.start > base[j].end:
                        j += 1
                    elif interval.end < base[j].start:
                        break
                    else:
                        tmp.append(Interval(max(interval.start, base[j].start), min(interval.end, base[j].end)))
                        if interval.end <= base[j].end:
                            break
                        else:
                            j += 1
                        
                base = tmp
        return base
                

if __name__ == "__main__":
    s = Solution()

    ret = s.getSolution([[Interval(1, 3)], [Interval(2, 6)]])
    for r in ret:
        print r
