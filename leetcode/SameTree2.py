
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node1.left = node2
    node1.right = node3

    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(2)
    node7 = TreeNode(3)
    node4.left = node5
    node4.right = node6
    node6.left = node7

    print s.isSameTree(node1, node4)
