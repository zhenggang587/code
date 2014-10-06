
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.traverse(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def traverse(self, preorder, pre_left, pre_right, inorder, in_left, in_right):
        if in_left > in_right:
            return None
        if in_left == in_right:
            return TreeNode(inorder[in_left])

        root_val = preorder[pre_left]
        root = TreeNode(root_val)

        index = in_left
        for index in range(in_left, in_right + 1):
            if inorder[index] == root_val:
                break

        left_len = index - in_left
        right_len = in_right - index

        if left_len > 0:
            root.left = self.traverse(preorder, pre_left + 1, pre_left + left_len, inorder, in_left, in_left + left_len - 1)
        if right_len > 0:
            root.right = self.traverse(preorder, pre_left + left_len + 1, pre_right, inorder, in_left + left_len + 1, in_right)
        return root

if __name__ == "__main__":
    s = Solution()

    node = s.buildTree([1], [1])

    print node.val
    print node.left.val
    print node.left.right.val
    print node.right.val
