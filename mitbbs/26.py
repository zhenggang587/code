
class Node:
    def __init__(self, x):
        self.val = x
        self.next = []

class Solution:
    def __init__(self):
        self.map = {}

    def getSolution(self, root):
        if not root:
            return None
        if root in self.map:
            return self.map[root]

        node = Node(root.val)
        self.map[root] = node
        for n in root.next:
            node.next = self.getSolution(n)
        return root


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
