
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.md5 = {}
        self.maxSize = 0
        self.first = self.second = None
        
    def getSolution(self, root):
        self.postorder(root)
        return self.first.val, self.second.val

    def postorder(self, root):
        if not root:
            return (0, '#') 

        (lsize, l) = self.postorder(root.left)
        (rsize, r) = self.postorder(root.right)

        s = str(root.val) + ' ' + l + ' ' + r
        size = lsize + rsize + 1
        if s in self.md5:
            if size > self.maxSize:
                self.maxSize = size
                self.first = root
                self.second = self.md5[s]
        else:
            self.md5[s] = root

        return (size, s)


if __name__ == "__main__":
    s = Solution()
    
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right = TreeNode(10)
    root.right.right = TreeNode(11)

    print s.getSolution(root)
