
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_sum = -(1 << 31)

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.postOrderTraverse(root) 

        return self.max_sum

    def postOrderTraverse(self, node):
        if not node:
            return 0

        left_sum = self.postOrderTraverse(node.left)
        right_sum = self.postOrderTraverse(node.right)

        sum = node.val
        if left_sum > 0:
            sum += left_sum
        if right_sum > 0:
            sum += right_sum

        self.max_sum = max(self.max_sum, sum)

        if max(left_sum, right_sum) > 0:
            return max(left_sum, right_sum) + node.val
        return node.val

        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(-1)
    node2 = TreeNode(0)
    node3 = TreeNode(-2)
    #node1.left = node2
    #node1.right = node3

    print s.maxPathSum(node1)

