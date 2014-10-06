
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.convert(num, 0, len(num) - 1)

    def convert(self, num, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(num[left]) 
        if right - left == 1:
            node = TreeNode(num[right])
            node.left = TreeNode(num[left])
            return node

        mid = left + (right - left) / 2
        node = TreeNode(num[mid])
        node.left = self.convert(num, left, mid - 1)
        node.right = self.convert(num, mid + 1, right)
        return node

        
if __name__ == "__main__":
    s = Solution()

    treenode = s.sortedArrayToBST([1, 2, 3, 4])
    print treenode.val
    print treenode.left.val
    print treenode.right.val
    print treenode.right.left.val
