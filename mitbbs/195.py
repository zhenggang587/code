
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):

    def traverse(self, node):
        if not node:
            return (0, 0)

        lpath, ldepth = self.traverse(node.left)
        rpath, rdepth = self.traverse(node.right)

        path = max(lpath, rpath, ldepth + rdepth + 1)

        return (path, max(ldepth, rdepth) + 1)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
