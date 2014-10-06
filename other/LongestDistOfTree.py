
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dist(self, root):
        if not root:
            return (0, 0) # height, max dist

        lh, ld = self.dist(root.left)
        rh, rd = self.dist(root.right)

        d = max(ld, rd, lh + rh + 1)
        return (max(lh, rh) + 1, d)

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(10)
    node2 = TreeNode(2)
    node3 = TreeNode(35)
    node1.right = node2
    node2.left = node3


    print s.dist(node1)
