
# see 166.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getSolution(self, root1, root2):


if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node1.left = node3
    node3.right = node2

    node4 = TreeNode(0)
    print s.getSolution(node1, node4)
