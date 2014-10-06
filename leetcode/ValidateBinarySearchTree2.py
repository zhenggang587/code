
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.traverse(root, -(1 << 31), (1 << 31))

    def traverse(self, node, lower, upper):
        if not node:
            return True

        return node.val > lower and node.val < upper \
                and self.traverse(node.left, lower, node.val) \
                and self.traverse(node.right, node.val, upper)


if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node1.left = node2
    #node1.right = node3
    #node2.right = node4

    print s.isValidBST(node1)
