
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        stack = [(root, 0)]
        deepLevel = 0
        deepNode = root
        while stack:
            (node, level) = stack.pop()
            if level > deepLevel:
                deepLevel = level
                deepNode = node

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return deepNode
            

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    
    print s.getSolution(node1).val
