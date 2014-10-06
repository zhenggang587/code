
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
        hasVisited = {}
        self.dfs(node, cloneNode, hasVisited)

        return cloneNode

    def dfs(self, node, cloneNode, hasVisited):
        if cloneNode.label not in hasVisited:
            hasVisited[cloneNode.label] = cloneNode
        else:
            return

        for neighbor in node.neighbors:
            tempNode = UndirectedGraphNode(neighbor.label) 
            if neighbor.label in hasVisited:
                tempNode = hasVisited[neighbor.label]

            cloneNode.neighbors.append(tempNode)
            self.dfs(neighbor, tempNode, hasVisited)
        
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
