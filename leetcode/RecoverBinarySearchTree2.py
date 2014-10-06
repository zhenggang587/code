
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pre = None
        self.first = None
        self.second = None

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root

    def traverse(self, node):
        if not node:
            return

        self.traverse(node.left)

        if self.pre and self.pre.val > node.val:
            if not self.first:
                self.first = self.pre
            self.second = node
        self.pre = node

        self.traverse(node.right)

    def printTree(self, root):
        if not root:
            return
        print root.val
        self.printTree(root.left)
        self.printTree(root.right)

        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(4)
    node1.left = node2
    node2.left = node3
    #node1.right = node3
    #node2.right = node4

    s.recoverTree(node1)
    s.printTree(node1)
