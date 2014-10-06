
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        INT_MIN = -(1 << 31)
        max_sum = [INT_MIN]
        self.postOrderTraverse(root, max_sum) 

        return max_sum[0]

    def postOrderTraverse(self, node, max_sum):
        left_sum = right_sum = -(1 << 31)
        if node.left:
            left_sum = self.postOrderTraverse(node.left, max_sum)
        if node.right:
            right_sum = self.postOrderTraverse(node.right, max_sum)

        sum = node.val
        if left_sum > right_sum and left_sum > 0:
            sum += left_sum
        elif right_sum > left_sum and right_sum > 0:
            sum += right_sum

        if left_sum > max_sum[0]:
            max_sum[0] = left_sum
        if right_sum > max_sum[0]:
            max_sum[0] = right_sum
        if sum > max_sum[0]:
            max_sum[0] = sum
        if left_sum + right_sum + node.val > max_sum[0]:
            max_sum[0] = left_sum + right_sum + node.val 

        return sum
        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(-1)
    node2 = TreeNode(0)
    node3 = TreeNode(-2)
    #node1.left = node2
    #node1.right = node3

    print s.maxPathSum(node1)

