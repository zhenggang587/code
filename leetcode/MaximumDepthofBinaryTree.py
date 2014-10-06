
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return self.traverse(root)

    def traverse(self, node):
        if not node:
            return 0

        left_depth = right_depth = 0
        if node.left:
            left_depth = self.traverse(node.left)
        if node.right:
            right_depth = self.traverse(node.right)

        depth = left_depth if left_depth > right_depth else right_depth
        return depth + 1
        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(1)
    #node1.left = node2
    #node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    #node4.left = node7
    #node4.right = node8
    #node6.right = node9

    print s.maxDepth(node1)
