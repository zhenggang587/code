
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        return self.traverse(root, root)

    def traverse(self, left_node, right_node):
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False

        return left_node.val == right_node.val \
                and self.traverse(left_node.left, right_node.right) \
                and self.traverse(left_node.right, right_node.left)
            

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    #node2.left = node4
    node2.right = node5
    #node3.left = node6
    node3.right = node7

    print s.isSymmetric(node1)
