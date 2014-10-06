
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self.dfs(node, {})

    def dfs(self, node, copied):
        if not node:
            return None
        if node in copied:
            return copied[node]

        cloneNode = UndirectedGraphNode(node.label)
        copied[node] = cloneNode

        for neighbor in node.neighbors:
            cloneNode.neighbors.append(self.dfs(neighbor, copied))

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
