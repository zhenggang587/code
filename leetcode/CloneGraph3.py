
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return

        cloneNode = UndirectedGraphNode(node.label)
        queue = [node]
        hasVisited = {node: cloneNode}
        while queue:
            n = len(queue)
            for i in range(len(queue)):
                cur = queue.pop(0)
                cloneCur = hasVisited[cur]
                for n in cur.neighbors:
                    if n in hasVisited:
                        cloneCur.neighbors.append(hasVisited[n])
                    else:
                        cloneN = UndirectedGraphNode(n.label)
                        hasVisited[n] = cloneN
                        cloneCur.neighbors.append(cloneN)
                        queue.append(n)
                
        return cloneNode

if __name__ == "__main__":
    s = Solution()
        
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node0.neighbors.append(node1)
    node0.neighbors.append(node2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node2)

    cloneNode0 = s.cloneGraph(node0)
    print cloneNode0.label
    print cloneNode0.neighbors[0].label
    print cloneNode0.neighbors[1].label
    print cloneNode0.neighbors[0].neighbors[0].label
    print cloneNode0.neighbors[0].neighbors[0].neighbors[0].label
    print cloneNode0.neighbors[0].neighbors[0].neighbors[0] == cloneNode0.neighbors[1]
    print cloneNode0.neighbors[0].neighbors[0] == cloneNode0.neighbors[1]
