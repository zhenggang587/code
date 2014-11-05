
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = None

    def getSolution(self, root):
        self.inorder(root)

        self.first.val , self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left):
        if self.pre and self.root.val < self.pre.val:
            if not self.first:
                self.first = self.pre
            self.second = self.root

        self.pre = root
        self.inorder(root.right)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
