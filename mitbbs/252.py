
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        paths = []
        self.traverse(root, 0, paths)
        return sum(paths)

    def traverse(self, root, val, paths):
        if not root:
            return
        val = val * 10 + root.val
        if not root.left and not root.right:
            paths.append(val)
            return

        self.traverse(root.left, val, paths)
        self.traverse(root.right, val, paths)
            

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    
    print s.getSolution(node1)
