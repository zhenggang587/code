
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True

        (height, is_balanced) = self.traverse(root)
        return is_balanced

    def traverse(self, node):
        left_height = right_height = 0
        is_balanced = True
        if node.left:
            (left_height, is_balanced) = self.traverse(node.left)
        if is_balanced and node.right:
            (right_height, is_balanced) = self.traverse(node.right)
        if not is_balanced:
            return (left_height, is_balanced)

        height = left_height if left_height > right_height else right_height
        height += 1

        if abs(left_height - right_height) <= 1:
            return (height, True)
        else:
            return (height, False)
        
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
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    #node4.left = node7
    #node4.right = node8
    node6.right = node9

    print s.isBalanced(node1)
