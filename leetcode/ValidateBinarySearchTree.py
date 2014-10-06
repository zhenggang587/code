
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
        if not root:
            return True
        flag, _, _ = self.traverse(root)
        return flag

    def traverse(self, node):
        if not node.left and not node.right:
            return True, node.val, node.val

        min_left = node.val
        if node.left:
            is_valid, min_left, max_left = self.traverse(node.left)
            if not is_valid or not node.val > max_left:
                return False, min_left, max_left

        max_right = node.val
        if node.right:
            is_valid, min_right, max_right = self.traverse(node.right)
            if not is_valid or not node.val < min_right:
                return False, min_right, max_right

        return True, min_left, max_right


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
