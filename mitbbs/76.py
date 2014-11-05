
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root1, root2):
        l = self.inorder(root1)
        r = self.inorder(root2)
        return l == r

    def inorder(self, root):
        stack = []
        p = root
        ret = []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                ret.append(p.val)
                p = p.right
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
