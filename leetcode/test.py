
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

class Solution:
    def cloneGraph(self, node):


    def dfs(self, node, hasVisited):
        if not node:
            return None
        if node in hasVisited:
            return hasVisited[node]

        cloneNode = UndirectedGraphNode(node.label)
        hasVisited[node] = cloneNode
        for neighbor in node.neighbors:
            cloneNode.neighbors.append(self.dfs(neighbor, hasVisited))

        return clo
     

if __name__ == "__main__":
    s = Solution()

