
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
        if not root:
            return True

        return self.traverse(root, root)

    def traverse(self, left_node, right_node):
        if left_node.val != right_node.val:
            return False

        if left_node.left and not right_node.right:
            return False
        elif not left_node.left and right_node.right:
            return False
        elif left_node.left and right_node.right:
            if not self.traverse(left_node.left, right_node.right):
                return False

        if left_node.right and not right_node.left:
            return False
        elif not left_node.right and right_node.left:
            return False
        elif left_node.right and right_node.left:
            if not self.traverse(left_node.right, right_node.left):
                return False
        return True
            

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
