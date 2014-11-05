
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        return self.traverse(root, -(1 << 31), (1 << 31))

    def traverse(self, node, low, high):
        if not node:
            return True

        return node.val > low and node.val < high \
                and self.traverse(node.left, low, node.val) \
                and self.traverse(node.right, node.val, high)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
