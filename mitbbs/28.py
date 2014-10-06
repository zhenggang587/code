
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMirror(self, root):
        if not root:
            return

        self.getMirror(root.left) 
        self.getMirror(root.right) 
        root.right, root.left = root.left, root.right

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    
    s.getMirror(node1)
    print node1.val
    print node1.left.val
    print node1.left.right.val

