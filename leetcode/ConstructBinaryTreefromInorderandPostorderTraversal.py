
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.traverse(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def traverse(self, inorder, in_left, in_right, postorder, post_left, post_right):
        if in_left > in_right:
            return None
        if in_left == in_right:
            return TreeNode(inorder[in_left])

        node_val = postorder[post_right]
        node = TreeNode(node_val)

        index = in_left
        for index in range(in_left, in_right + 1):
            if inorder[index] == node_val:
                break

        left_len = index - in_left
        right_len = in_right - index
        if left_len > 0:
            node.left = self.traverse(inorder, in_left, index - 1, postorder, post_left, post_left + left_len - 1)
        if right_len > 0:
            node.right = self.traverse(inorder, index + 1, in_right, postorder, post_left + left_len, post_right - 1)
        return node 
        

if __name__ == "__main__":
    s = Solution()

    node = s.buildTree([2, 3, 1, 4], [3, 2, 4, 1])

    print node.val
    print node.left.val
    print node.left.right.val
    print node.right.val
        
