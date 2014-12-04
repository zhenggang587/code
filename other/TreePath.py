
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def getSolution(self, root):
        if not root:
            return []
        stack = [root]
        paths = []
        hasVisited = set([root])
        while stack:
            cur = stack[-1]
            while cur.left and cur.left not in hasVisited:
                cur = cur.left
                stack.append(cur)
                hasVisited.add(cur)

            if not cur.left and not cur.right:
                paths.append(self.addResult(stack))
                stack.pop()
            elif cur.right and cur.right not in hasVisited:
                cur = cur.right
                stack.append(cur)
                hasVisited.add(cur)
            else:
                stack.pop()
        return paths
    
    def addResult(self, stack):
        path = []
        for node in stack:
            path.append(node.val)
        return ''.join(path)

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode('A')
    node2 = TreeNode('B')
    node3 = TreeNode('C')
    #node1.left = node2
    node1.right = node3

    node4 = TreeNode('E')
    node5 = TreeNode('F')
    node3.left = node4
    node3.right = node5

    print s.getSolution(node1)
