
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        return self.traverse(root, root)
    
    def traverse(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        return node1.val == node2.val \
                and self.traverse(node1.left, node2.right) \
                and self.traverse(node1.right, node2.left)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
