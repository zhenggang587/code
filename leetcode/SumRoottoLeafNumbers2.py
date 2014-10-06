
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node, val):
        if not node:
            return
        if not node.left and not node.right:
            self.sum += val * 10 + node.val
            return

        self.dfs(node.left, val * 10 + node.val)
        self.dfs(node.right, val * 10 + node.val)
        

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    print s.sumNumbers(node1)


